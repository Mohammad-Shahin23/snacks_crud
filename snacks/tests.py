
# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Snacks


class SnackssTests(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester",password="tester")
        Snacks.objects.create(name="rake", purchaser=reviewer)

    def test_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks.html')
        self.assertTemplateUsed(response, 'base.html')

    # def test_list_page_context(self):
    #     url = reverse('snacks')
    #     response = self.client.get(url)
    #     Snacks = response.context['snacks']
    #     self.assertEqual(len(Snacks), 1)
    #     self.assertEqual(Snacks[0].name, "rake")
    #     self.assertEqual(Snacks[0].description, 0)
    #     self.assertEqual(Snacks[0].reviewer.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('snacks_details',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snacks_details',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_details.html')
        self.assertTemplateUsed(response, 'base.html')

