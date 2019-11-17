from django.test import TestCase
from . models import *

class ImageTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Image Model.
    '''
    
    def setUp(self):
        self.profile_one = Profile(profile_photo='images/mine.jpg',bio='Currently doing datascience in moringa')
        self.profile_one.save_profile()
        self.image_one = Image(image='images/lagoon.jpeg',image_name='dan', image_caption='lacasa de papel',comments='aaaaawww!',likes=40, id=1,profile=self.profile_one)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image_one,Image)) 

    def test_save_method(self):
        
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) is 0)
        
    def test_update_method(self):
        self.image_one.save()
        new_caption = 'That image is cool'
        done = self.image_one.update_caption(self.image_one.id,new_caption)
        self.assertEqual(done,new_caption)
        
class ProfileTestClass(TestCase):
    
    '''
    This is a class that perform unnittest  behaviour on the Profile Model.
    '''
    
    def setUp(self):
        self.profile_one = Profile(profile_photo='images/mine.jpg',bio='Currently doing datascience in moringa')
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_one,Profile)) 

    def test_save_method(self):
        
        self.profile_one.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile_one.save_profile()
        self.profile_one.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) is 0)
        
    def test_update_method(self):
        self.profile_one.save_profile()
        new_bio = '# thursday speaker'
        done = self.profile_one.update_bio(self.profile_one.id,new_bio)
        self.assertEqual(done,new_bio)
    
    