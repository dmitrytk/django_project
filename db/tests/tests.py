import os

from django.test import TestCase
from ..models import OilField, Well
from ..load import upload_wells


class DatabaseTests(TestCase):
    def test_well_load(self):
        with open('db/tests/wells.txt', 'r') as file:
            content = file.read()

        upload_wells(content)

        wells = Well.objects.all()
        self.assertEqual(len(wells), 6)
        self.assertEqual(wells[0].name, '1051')
