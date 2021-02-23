from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_Profile_Images(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user_profile_images/')

# class Playlists(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     playlists_name = models.CharField(max_length=100)

class Songs(models.Model):
    song_file = models.FileField(upload_to='song_files/')

class Songs_Metadata(models.Model):
    song_id = models.ForeignKey(Songs, on_delete=models.CASCADE, unique=True)
    album_name= models.CharField(max_length=80)
    album_img = models.ImageField(upload_to='album_images/')
    artist_name = models.CharField(max_length=50)
    genre_name = models.CharField(max_length=50, default="miscellaneous")


class Captured_Images(models.Model): 
    user_face_image = models.ImageField(upload_to='images/') 