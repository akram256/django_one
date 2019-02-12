from rest_framework import status
import json
from django.test import TestCase,Client
from blogpost.models import Puppy
from django.urls import reverse
from blogpost.serializers import PuppySerializer

client = Client()

class CreatePuppyTest(TestCase):
    

    def setUp(self):
        
        self.valid_payload={
            'name':'rambo',
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
    
    