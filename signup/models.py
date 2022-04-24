from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='doctprofile/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
class Address(models.Model):
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=100)

