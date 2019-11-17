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
        

    
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images')
    bio = models.TextField()
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    def update_bio(self):
        pass