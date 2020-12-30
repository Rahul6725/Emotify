from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_Profile_Images(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user_profile_images/')

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    genre_img = models.ImageField(upload_to='genre_images/')
    description = models.TextField()

class Playlists(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    playlists_name = models.CharField(max_length=100)

class Artists(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=50)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    song_id = models.IntegerField(default=-1)

class Songs(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    artist_id = models.ForeignKey(Artists, on_delete=models.CASCADE)
    duration = models.TimeField(auto_now=False, auto_now_add=False)

class Albums(models.Model):
    album_name = models.CharField(max_length=50)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artists, on_delete=models.CASCADE)
    album_img = models.ImageField(upload_to='album_images/')
    description = models.TextField()
    song_id = models.ForeignKey(Songs, on_delete=models.CASCADE)



class Captured_Images(models.Model): 
    user_face_image = models.ImageField(upload_to='images/') 