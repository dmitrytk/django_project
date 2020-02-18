from django.db import IntegrityError
from .models import OilField, Well
from .utils import *


# MAIN WELL LOAD METHOD
def upload_wells(wells_data):
    if validate_string(wells_data):
        header, body = get_table(wells_data)
        if check_header(header, columns, ['well', 'field']):
            df = create_df(header, body)
            wells = create_well_list(df)
            if len(wells) > 0:
                Well.objects.bulk_create(wells, ignore_conflicts=True)
                print('\n\n\nSUCCESS\n\n\n')


# MAIN OIL FIELD LOAD METHOD
def upload_fields(fields_data):
    pass
