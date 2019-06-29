from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class userinfo(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email_ID = models.EmailField()
    Mobile_No = models.IntegerField()
    Date_Of_Birth = models.DateField()
    Photo = models.ImageField(upload_to='pict')
    Remark = models.TextField()

def __str__(self):
    return self.First_name

class registration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField()
    city = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()

def __str__(self):
    return self.phone
