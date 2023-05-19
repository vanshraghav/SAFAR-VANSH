from django.db import models


# Create your models here.
class Delhi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    desc_field = models.TextField()

class Mumbai(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    desc_field = models.TextField()
    
class Chennai(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    desc_field = models.TextField()

class Surat(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    desc_field = models.TextField()
   
class Contact(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    subject =models.CharField(max_length=100)
    message=models.TextField()
