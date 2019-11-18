from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod    
    def update_caption(cls,id,new_caption):
        cls.objects.filter(pk = id ).update(image_caption = new_caption)
        new_caption_object = cls.objects.get(image_caption=new_caption)
        new_caption = new_caption_object.image_caption
        return new_caption
    
    
        
        

    
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod   
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio
        