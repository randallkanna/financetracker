from django.test import TestCase
from .models import List

class ModelTestCase(TestCase):
    def setUp(self):
        self.list_name = "Test"
        self.list = List(name=self.list_name)

    def test_model_can_create_a_list(self):
        old_count = List.objects.count()
        self.list.save()
        new_count = List.objects.count()
        self.assertNotEqual(old_count, new_count)