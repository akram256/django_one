from rest_framework import status
import json
from django.test import TestCase,Client
from blogpost.models import Puppy
from django.urls import reverse
from blogpost.serializers import PuppySerializer

client = Client()

class CreatePuppyTest(TestCase):
    

    def setUp(self):
        self.casper=Puppy.objects.create(name="Casper",
            age=12,breed="bull dog", color="black")
        self.muffin=Puppy.objects.create(name="muffy", age=3,breed="gradane",color="white")
        
        self.valid_payload={
            'name':'muffy',
            'age':12,
            'breed':'Pamerion',
            'color':'black'
        }
        self.invalid_payload={
            'name':'',
            'age':12,
            'breed':'Pamerion',
            'color':'black'
        }

    def test_create_valid_puppies(self):
        response = client.post(reverse('get_post_puppy'),
        data =json.dumps(self.valid_payload),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppies(self):
        response = client.post(reverse('get_post_puppy'),
        data =json.dumps(self.invalid_payload),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_update_valid_puppies(self):
        response = client.put(reverse('get_delete_update_puppy', kwargs={'pk':self.muffin.pk}),
        data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_invalid_puppies(self):
        response = client.put(reverse('get_delete_update_puppy', kwargs={'pk':self.muffin.pk}),
        data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_puppies(self):
        response = client.delete(reverse('get_delete_update_puppy',kwargs={'pk':self.muffin.pk}),
        data = json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_puppies(self):
        response= client.delete(reverse('get_delete_update_puppy',kwargs={'pk': 30}),
        data=json.dumps(self.invalid_payload),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    