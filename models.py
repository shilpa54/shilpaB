from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class chefregmodel(models.Model):
    fname=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=20)

class nonmodel(models.Model):
    nitem=models.CharField(max_length=20)
    ndis=models.CharField(max_length=5000)
    nimage=models.FileField(upload_to='cookingapp/static/nonveg')
class vmodel(models.Model):
   vitem=models.CharField(max_length=20)
   vprice=models.IntegerField()
   vdis=models.CharField(max_length=5000)
   vimage=models.FileField(upload_to='cookingapp/static/veg')


class userregmodel(models.Model):
    fullname=models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password=models.CharField(max_length=20)

