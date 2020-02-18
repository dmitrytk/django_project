from .models import OilField, Well
from .columns import columns, valid_columns, float_types
import time


def _to_float(val):
    """Convert input string to float. If error return None"""
    try:
        num = float(val.strip().replace(' ', '').replace(',', '.'))
    except ValueError as e:
        num = None
    return num


def validate_string(content):
    """Validate multiline string with TAB separator"""
    return len(content) > 10 and '\n' in content and '\t' in content


def get_table(content):
    """Get header (list) and body (2d list) from input string"""
    rows = content.split('\n')

    header = rows[0].strip().split('\t')
    header_length = len(header)

    body = []
    for row in rows[1:]:
        r = row.strip().split('\t')
        if len(r) == header_length:
            body.append(r)

    print(body)
    return header, body


def prepare_header(header, columns, required_columns, wells_load=True):
    # Change column names
    for index, col in enumerate(header):
        for key in columns:
            if col.lower() in columns[key]:
                header[index] = key
    print(header)
    # check if all columns is valid
    if all([col in columns for col in header]) and all([col in header for col in required_columns]):
        if wells_load:
            header[header.index('well')] = 'name'
        else:
            header[header.index('field')] = 'name'
        return True
    else:
        return False


def create_df(header, body, float_columns=float_types):
    """Create dataframe from header and body"""
    df = {}
    for index, col in enumerate(header):
        df[col] = [row[index] for row in body]
    for col in df:
        if col in float_columns:
            df[col] = [_to_float(i) for i in df[col]]
    return df


def create_well_list(df):
    """List of Well model from dataframe"""
    # load fields from db
    fields = OilField.objects.all()
    fields = {field.name: field for field in fields}

    # load wells from db
    old_wells = Well.objects.all()
    old_wells = {f'{well.name} {well.field.name}': well for well in old_wells}

    fields_input = list(set(df['field']))

    # check for new fields
    new_fields = []
    for field in fields_input:
        if fields.get(field) is None:
            new_fields.append(OilField(name=field))

    # create new fields if any
    if len(new_fields) > 0:
        OilField.objects.bulk_create(new_fields, ignore_conflicts=True)
        fields = OilField.objects.all()
        fields = {field.name: field for field in fields}

    # create well list
    new_wells = []
    for index, row in enumerate(df['name']):
        well_name = df['name'][index]
        field = fields.get(df['field'][index])

        well = old_wells.get(f'{well_name} {field.name}')
        if well is not None:
            for attr in df:
                if attr != 'name' and attr != 'field':
                    setattr(well, attr, df[attr][index])
            well.save()
        else:
            well = Well(name=well_name, field=field)
            for attr in df:
                if attr != 'name' and attr != 'field':
                    setattr(well, attr, df[attr][index])
            new_wells.append(well)

    return new_wells, old_wells
