from django.db import IntegrityError
from .models import OilField, Well
from .utils import (validate_string, get_table, prepare_header, create_df,
                    create_wells_list, delete_excess_cols, save_fields)
from .columns import valid_columns
import time


# MAIN WELL LOAD METHOD

def upload_wells(wells_data):
    if validate_string(wells_data):
        header, body = get_table(wells_data)
        if prepare_header(header, valid_columns, ['well', 'field']):
            df = create_df(header, body)
            delete_excess_cols(df, valid_columns)
            new_wells = create_wells_list(df)
            if len(new_wells) > 0:
                Well.objects.bulk_create(new_wells, ignore_conflicts=True)
        else:
            print('WELLS NOT LOADED')


# MAIN OIL FIELD LOAD METHOD
def upload_fields(fields_data):
    if validate_string(fields_data):
        header, body = get_table(fields_data)
        if prepare_header(header, valid_columns, ['field'], False):
            df = create_df(header, body)
            delete_excess_cols(df, valid_columns)
            save_fields(df)
