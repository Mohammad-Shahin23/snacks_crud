
# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snacks



class SnackssTests(TestCase):
   
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@gmail.com',
            ps = '1234',
        )
        self.snack = Snacks.objects.create(
            name ='chips',
            description  = "good",
            purchaser = self.user, 
        )
    
    def test_str_method(self):
        self.assertEqual(str(self.snack),"test")

    def test_detail_view(self):
        url = reverse('snacks_details', args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snacks_details.html')

    def test_create_view(self):
        obj={
            'name':"test2",
            'description'  : "good",
            'purchaser' : self.user.id, 
        }

        url = reverse('snacks_create')
        response = self.client.post(path=url,data=obj,follow=True)
        # self.assertEqual(len(Thing.objects.all()),2)
        self.assertRedirects(response, reverse('snacks_details', args=[2]))
