from django.test import TestCase
from .models import OilField, Well

class DBTests(TestCase):
    def test_OilField(self):
        field = OilField.objects.create(
            name='Pokamas',
            type='oil',
            location='surgut',
            owner='slavneft',
        )
        self.assertEqual(field.name, 'Pokamas')
        self.assertEqual(field.type, 'oil')
        self.assertEqual(field.owner, 'slavneft')
        

    def test_Well(self):
        field = OilField.objects.create(
            name='Pokamas',
            type='oil',
            location='surgut',
            owner='slavneft',
        )
        well = Well.objects.create(
            name='11W',
            field=field,
            type='production',
        )
        self.assertEqual(well.name, '11W')
        self.assertEqual(well.type, 'production')
        