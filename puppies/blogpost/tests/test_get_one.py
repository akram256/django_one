from rest_framework import status
from django.test import TestCase,Client
from blogpost.models import Puppy
from django.urls import reverse
from blogpost.serializers import PuppySerializer

client = Client()

class GetSinglePuppyTest(TestCase):
    

    def setUp(self):
        self.rambo=Puppy.objects.create(name="rambo",
            age=12,breed="bull dog", color="black")
        self.ricky=Puppy.objects.create(name="ricky", age=3,breed="gradane",color="white")

    def test_get_a_valid_single_puppy(self):
        response = client.get(reverse('get_delete_update_puppy',kwargs={'pk':self.rambo.pk}))
        puppy= Puppy.objects.get(pk=self.rambo.pk)
        serializers = PuppySerializer(puppy)
        self.assertEqual (response.data, serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_puppy(self):
        response=client.get(reverse('get_delete_update_puppy',kwargs={'pk':30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)