from django.test import TestCase
from .models import OilField, Well


class DatabaseTests(TestCase):
    def setUp(self):
        self.field = OilField.objects.create(
            name='Pokamas',
            type='oil',
            location='surgut',
            owner='slavneft',
        )
        self.well = Well.objects.create(
            name='11W',
            field=self.field,
            type='production',
        )

    def test_OilField(self):
        self.assertEqual(self.field.name, 'Pokamas')
        self.assertEqual(self.field.type, 'oil')
        self.assertEqual(self.field.owner, 'slavneft')

    def test_Well(self):
        self.assertEqual(self.well.name, '11W')
        self.assertEqual(self.well.type, 'production')
