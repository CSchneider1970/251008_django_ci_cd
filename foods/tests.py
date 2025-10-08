from django.test import TestCase
from .models import Food


class FoodTest(TestCase):

    def test_creation(self):
        # the test is okay - make it work after you have pushed to github
        food_ = Food.objects.create(name='papaya', description='Healthy yellow fruit')
        self.assertDictEqual({'name': 'papaya', 'description': 'Healthy yellow fruit'}, food_.to_dictionary())
