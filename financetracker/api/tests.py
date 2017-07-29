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

    def test_api_can_get_a_list(self):
        list = List.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': list.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, list)

    def test_api_can_update_list(self):
        change_list = {'name': 'newName'}

        res = self.client.put(
            reverse('details', kwargs={'pk': list.id}),
            change_list, format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_list(self):
        list = List.objects.get()

        response = self.client.dete(
            reverse('details', kwargs={'pk: list.id'}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
