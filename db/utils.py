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


# MAIN WELL LOAD METHOD
def upload_wells(wells_data):
    pass


# MAIN OIL FIELD LOAD METHOD
def upload_fields(fields_data):
    pass
