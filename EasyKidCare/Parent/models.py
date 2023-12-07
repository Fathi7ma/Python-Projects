from django.db import models


class Parent_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Phoneno=models.CharField(max_length=20)
    File=models.FileField(default="")
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
class Student_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20,default="abc")
    Age=models.CharField(max_length=20)
    Image=models.FileField(max_length=20)
    FatherName=models.CharField(max_length=20)
    MotherName=models.CharField(max_length=20)
    Parentid=models.ForeignKey(Parent_tb,on_delete=models.CASCADE,null=True)
    Phoneno=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
class sponsership_tb(models.Model):
    SponserName=models.CharField(max_length=20)
    Job=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    SponserItem=models.CharField(max_length=20)
class Vaccination_tb(models.Model):
    Date=models.CharField(max_length=20)
    VaccinationName=models.CharField(max_length=20)
    Place=models.CharField(max_length=20)
    studentid=models.ForeignKey('Parent.Student_tb',on_delete=models.CASCADE,null=True)

