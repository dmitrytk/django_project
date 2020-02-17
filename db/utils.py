from django.db import IntegrityError
from .models import OilField, Well

valid_columns = {
    'well': 'str',
    'field': 'str',
    'type': 'str',
    'location': 'str',
    'owner': 'str',
    'alt': 'float',
    'md': 'float',
    'x': 'float',
    'y': 'float',
}

float_columns = [
    'x',
    'y',
    'alt',
    'md',
]


def check_column_names(header, valid_columns):
    for col in header:
        if valid_columns.get(col) is None:
            return False
    if 'field' not in header:
        return False
    return True


def get_data(input_data):
    input_data = input_data.replace('\r', '')
    rows = [row.split('\t') for row in input_data.split('\n')]
    # Header
    header = rows[0]
    header_length = len(header)

    if not check_column_names(header, valid_columns):
        raise ValueError('Column names not valid')
    # Data
    data = [row for row in rows[1:] if len(row) == header_length]

    return {
        'header': header,
        'data': data
    }


def get_wells_list(data, fields):
    wells = []
    for row in data['data']:
        well = Well(well=well, )
        for index, col in enumerate(data['header']):
            setattr(well, col, row[index])
        wells.append(well)
    return wells


def get_fields_list(data):
    fields = []
    for row in data['data']:
        field = OilField()
        for index, col in enumerate(data['header']):
            setattr(field, col, row[index])
        fields.append(field)
    return fields


# MAIN WELL LOAD METHOD
def upload_wells(wells_data):
    wells_data = get_data(wells_data)

    fields = OilField.objects.all()
    fields_dict = {field.name: field for field in fields}

    field_column = wells_data['header'].index('field')
    fields_input = list(set([row[field_column] for row in wells_data['data']]))

    # Create new Oil field if not in DB
    new_fields = []
    for field in fields_input:
        if fields_dict.get(field) is None:
            new_fields.append(OilField(field=field))
    if len(new_fields) > 0:
        OilField.objects.bulk_create(new_fields)

        # Get fields from DB again
        fields = OilField.objects.all()
        fields_dict = {field.name: field for field in fields}


# MAIN OIL FIELD LOAD METHOD
def upload_fields(fields_data):
    pass
