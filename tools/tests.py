from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import sub



class StaticPagesTests(SimpleTestCase):
    def test_sub(self):
        response = self.client.get(reverse('sub'))
        self.assertEqual(response.status_code, 200)
        # Check template used
        self.assertTemplateUsed(response, 'tools/sub.html')
        # Contains assertion
        self.assertContains(response, 'Срезки от соседних водозаборов')
        self.assertNotContains(response, 'Some random text')
        # resolve - return view function of url
        view = resolve(reverse('sub'))
        self.assertEqual(view.func.__name__, sub.__name__)

    def test_distance(self):
        response = self.client.get(reverse('distance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools/distance.html')

    def test_roxar(self):
        response = self.client.get(reverse('roxar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools/roxar.html')

    def test_water(self):
        response = self.client.get(reverse('water'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools/water.html')

    def test_print(self):
        response = self.client.get(reverse('print'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools/print.html')


