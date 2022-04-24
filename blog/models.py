from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.forms import CharField

# Create your models here.
class Blog(models.Model):
    img = models.ImageField(upload_to='blogImages/')
    caption = models.CharField(max_length=500)
    postDate = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.caption
class Appointment(models.Model):
    req_spec = models.CharField(max_length=100)
    doa = models.DateField()
    sta = models.TimeField()

    def __str__(self):
        return self.req_spec

class DocAppointments(models.Model):
    docuser = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

class PatAppointments(models.Model):
    patuser = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)