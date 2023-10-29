from django.db import models

# Create your models here.
class login_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class register_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)

class form_tb(models.Model):
    Name=models.CharField(max_length=20)
    Dob=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Phonenumber=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Department=models.CharField(max_length=20)
    Courses=models.CharField(max_length=20)
    Materials=models.CharField(max_length=20)
