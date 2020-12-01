from django.test import TestCase
from django.urls import reverse


class HomepageTest(TestCase):
    def test_homepage(self):
        """Verify that the homepage can be accessed"""
        response = self.client.get(reverse('cinema:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Kino')
