from django.test import TestCase
from .models import List
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    def setUp(self):
        self.list_name = "Test"
        self.list = List(name=self.list_name)

    def test_model_can_create_a_list(self):
        old_count = List.objects.count()
        self.list.save()
        new_count = List.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_data = {'name': 'Test'}
        self.response = self.client.post(
            reverse('create'),
            self.list_data,
            format="json")

    def test_api_can_create_a_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

