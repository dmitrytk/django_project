from django.db import IntegrityError
from .models import OilField, Well


def upload_wells(wells_data):
    wells_data = wells_data.replace('\r', '')
    fields = OilField.objects.all()
    fields_dict = {field.name: field for field in fields}
    rows = wells_data.split('\n')

    if len(rows) > 1:
        header = rows[0].split('\t')
        header_length = len(header)

        arr = [row.split('\t') for row in rows[1:]]
        arr = [row for row in arr if len(row) == header_length]

        columns_dict = {value: index for index, value in enumerate(header)}

        # get all oil fields from input data
        input_fields = list(set([row[columns_dict['field']] for row in arr]))

        # Create new oil fields
        for field in input_fields:
            if not field in fields_dict:
                OilField.objects.create(name=field)

        fields = OilField.objects.all()
        fields_dict = {field.name: field for field in fields}

        for row in arr:
            field_name = row[columns_dict['field']]
            well_name = row[columns_dict['well']]
            try:
                well = Well.objects.create(name=well_name, field=fields_dict[field_name])
                well.md = float(row[columns_dict['md']])
                well.save()
            except IntegrityError as e:
                pass


def upload_fields(fields_data):
    pass
