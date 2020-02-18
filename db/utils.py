from .models import OilField, Well

columns = [
    'field',
    'type',
    'location',
    'owner',
    'well',
    'alt',
    'md',
    'x',
    'y'
]


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

    return header, body


def check_header(header, columns, required_columns):
    """Check header for required columns"""
    return all([col in columns for col in header]) and all([col in header for col in required_columns])


def create_df(header, body, float_types=['x', 'y', 'alt', 'md']):
    """Create dataframe from header and body"""
    df = {}
    for index, col in enumerate(header):
        df[col] = [row[index] for row in body]
    for col in df.keys():
        if col in float_types:
            df[col] = [_to_float(i) for i in df[col]]
    return df


def create_well_list(df):
    """List of Well model from dataframe"""
    fields = OilField.objects.all()
    fields = {field.name: field for field in fields}
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
    wells = []
    for index, row in enumerate(df['well']):
        well = Well()
        for attr in df.keys():
            if attr == 'field':
                well.field = fields.get(df['field'][index])
            elif attr == 'well':
                well.name = df['well'][index]
            else:
                setattr(well, attr, df[attr][index])

        if well.name is not None and well.field is not None:
            wells.append(well)
    return wells
