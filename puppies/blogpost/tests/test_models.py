from django.test import TestCase
from blogpost.models import Puppy

class PuppyTest(TestCase):
    

    def setUp(self):
        Puppy.objects.create(name="dog",
            age=12,breed="bull dog", color="black")
        Puppy.objects.create(name="bdog", age=3,breed="gradane",color="white")

    def test_puppy_breed(self):
        puppy_dog =Puppy.objects.get(name="dog")
        puppy_bdog = Puppy.objects.get(name="bdog")
        self.assertEqual(puppy_dog.get_breed(),"dog belongs to bull dog breed")
        self.assertEqual(puppy_bdog.get_breed(), "bdog belongs to gradane breed")


