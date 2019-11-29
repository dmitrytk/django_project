from django.test import TestCase, SimpleTestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_sub_page_status_code(self):
        response = self.client.get('/tools/sub/')
        self.assertEqual(response.status_code, 200)

    def test_distance_page_status_code(self):
        response = self.client.get('/tools/distance/')
        self.assertEqual(response.status_code, 200)
