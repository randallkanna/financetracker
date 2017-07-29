from django.test import TestCase
from .models import List
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test")
        self.list_name = "Test"
        self.list = List(name=self.list_name, owner=user)

    def test_model_can_create_a_list(self):
        old_count = List.objects.count()
        self.list.save()
        new_count = List.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="Test")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.list_data = {'name': 'Test', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.list_data,
            format="json")

    def test_api_can_create_a_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/lists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_list(self):
        list = List.objects.get(id=1)
        response = self.client.get(
            '/bucketlists/',
            kwargs={'pk': bucketlist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, list)

    def test_api_can_update_a_list(self):
        list = List.objects.get()
        change_list = {'name': 'new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': list.id}),
            change_list, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_a_list(self):
        list = List.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': list.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
