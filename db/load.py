from django.db import IntegrityError
from .models import OilField, Well
from .utils import *
import time


# MAIN WELL LOAD METHOD

def upload_wells(wells_data):
    start = time.time()
    if validate_string(wells_data):
        header, body = get_table(wells_data)
        if prepare_header(header, columns, ['well', 'field']):
            df = create_df(header, body)
            new_wells, old_wells = create_well_list(df)
            if len(new_wells) > 0:
                Well.objects.bulk_create(new_wells, ignore_conflicts=True)
                print('\n\n\nSUCCESS\n\n\n')
        else:
            print('WRONG HEADER')

    print(f'\n\n\nTIME ELAPSED {time.time() - start}\n\n\n')


# MAIN OIL FIELD LOAD METHOD
def upload_fields(fields_data):
    pass
