from django.db import models

class user(models.Model):
    username = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    profile_photo_path = models.CharField(max_length=1000)
    birthdate = models.DateField( blank=True )
    