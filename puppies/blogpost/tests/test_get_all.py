from rest_framework import status
from django.test import TestCase,Client
from blogpost.models import Puppy
from django.urls import reverse
from blogpost.serializers import PuppySerializer

client = Client()

class GetAllPuppyTest(TestCase):
    

    def setUp(self):
        Puppy.objects.create(name="dog",
            age=12,breed="bull dog", color="black")
        Puppy.objects.create(name="bdog", age=3,breed="gradane",color="white")

    def test_get_all_puppies(self):
        response = client.get(reverse('get_post_puppy'))
        puppies = Puppy.objects.all()
        serializers = PuppySerializer(puppies, many=True)
        self.assertEqual (response.data, serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)