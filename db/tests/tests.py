import os

from django.test import TestCase
from ..models import OilField, Well
from ..load import upload_wells, upload_fields


class DatabaseTests(TestCase):
    def test_wells_load(self):
        with open('db/tests/wells.txt', 'r') as file:
            content = file.read()
        upload_wells(content)

        wells = Well.objects.all()
        self.assertEqual(len(wells), 6)
        self.assertEqual(wells[0].name, '1051')

    def test_fields_load(self):
        with open('db/tests/fields.txt', 'r') as file:
            content = file.read()
        upload_fields(content)

        fields = OilField.objects.all()
        self.assertEqual(fields[0].name, 'Vadelyp')
        self.assertEqual(fields[0].type, 'oil')
