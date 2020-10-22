from django.db import models

# Create your models here.
class Captured_Images(models.Model): 
    user_face_image = models.ImageField(upload_to='images/') 