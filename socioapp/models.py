from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=50)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod    
    def update_caption(cls,id,new_caption):
        cls.objects.filter(id = id ).update(image_caption = new_caption)
        

    
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images')
    bio = models.TextField()
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod   
    def update_bio(cls,id,new_bio):
        cls.objects.filter(id = id).update(bio=new_bio)
        pass