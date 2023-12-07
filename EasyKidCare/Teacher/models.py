from django.db import models

class Teacher_tb(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    Phoneno=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Qualifications=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
    File=models.FileField(default="")
class Activity_tb(models.Model):
    Item=models.CharField(max_length=20)
    Description=models.CharField(max_length=20)
    File=models.FileField(max_length=20,default=1)
    Date=models.CharField(max_length=20,default=1)
class DailyActivity_tb(models.Model):
    Activity=models.CharField(max_length=20,default=1)
    Food=models.CharField(max_length=20)
    SleepingTime=models.CharField(max_length=20)
    Games=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
class Event_tb(models.Model):
    Event_name=models.CharField(max_length=20)
    Description=models.CharField(max_length=20)
    Venue=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Food=models.CharField(max_length=20)
class Attendence_tb(models.Model):
    Date=models.CharField(max_length=20)
class Present_tb(models.Model):
    Date=models.CharField(max_length=20,default="")
    Attendenceid=models.ForeignKey('Attendence_tb',on_delete=models.CASCADE,null=True)
    Studentid=models.ForeignKey('Parent.Student_tb',on_delete=models.CASCADE,null=True)
class Absent_tb(models.Model):
    Date=models.CharField(max_length=20,default="")
    Attendenceid=models.ForeignKey('Attendence_tb',on_delete=models.CASCADE,null=True)
    Studentid=models.ForeignKey('Parent.Student_tb',on_delete=models.CASCADE,null=True)
class FoodShedule_tb(models.Model):
    Snack=models.CharField(max_length=20)
    Lunch=models.CharField(max_length=20)
    Eveningsnack=models.CharField(max_length=20)
    Date=models.CharField(max_length=20,default=1)
class Mother_tb(models.Model):
    Mother_name=models.CharField(max_length=20)
    Dob=models.CharField(max_length=20,default="abc")
    Details=models.CharField(max_length=50)
    Phoneno=models.CharField(max_length=20)
    Address=models.CharField(max_length=30)
    Height=models.CharField(max_length=30,default="abc")
    Weight=models.CharField(max_length=30,default="abc")
    Hemoglobin=models.CharField(max_length=30,default="abc")
    Nutritions=models.ForeignKey('Nutritions_tb',on_delete=models.CASCADE,null=True)
    Thr=models.ForeignKey('THR_tb',on_delete=models.CASCADE,null=True)
class Nutritions_tb(models.Model):
    Name=models.CharField(max_length=20)
class THR_tb(models.Model):
    Item=models.CharField(max_length=30)
    Quantity=models.CharField(max_length=30)
class LactatingWoman_tb(models.Model):
    Name=models.CharField(max_length=20)
    Dob=models.CharField(max_length=20)
    Phoneno=models.CharField(max_length=20)
    Deliverydate=models.CharField(max_length=20)
    Infantgender=models.CharField(max_length=20)
    Thr=models.ForeignKey('THR_tb',on_delete=models.CASCADE,null=True)
class GrowthDetails_tb(models.Model):
    Name=models.CharField(max_length=20)
    Date_of_birth=models.CharField(max_length=20)
    Birth_reg_no=models.CharField(max_length=20)
    Fathername=models.CharField(max_length=20)
    Mothername=models.CharField(max_length=20)
    Family_survey_regno=models.CharField(max_length=20)







