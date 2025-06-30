from django.db import models

# Create your models here.

class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class DoctorInfo(models.Model):
    dr_name=models.CharField(max_length=100)
    dr_image=models.ImageField(upload_to='doctors/')
    specialization=models.CharField(max_length=100)

    def __str__(self):
        return self.dr_name
    
class Register(models.Model):
    d_name=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100) 
    p_age=models.IntegerField()
    p_gender=models.CharField(max_length=100)
    p_contact=models.IntegerField()
    problem=models.CharField(max_length=100)

    def __str__(self):
        return self.p_name
