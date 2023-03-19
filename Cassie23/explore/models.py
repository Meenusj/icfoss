from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=60)
    about = models.TextField()
    avgrating=models.DecimalField(max_digits=15,decimal_places=10)
    behaviour=models.IntegerField()
    toiletandcleanliness=models.IntegerField()
    inhousestay=models.BooleanField()
    disableperson_friendly=models.BooleanField()
    medical_emergency=models.BooleanField()
    food_facility=models.IntegerField()
    opstarting=models.TimeField()
    opending=models.TimeField()
    working_days=models.CharField(max_length=30,default='S' 'M' 'T' 'W' 'T' 'F' 'S')
    feechild=models.FloatField()
    feeadult=models.FloatField()
    feeforeigner=models.FloatField()
    feestudent=models.FloatField()
    latitude=models.FloatField()
    longitude=models.FloatField()


# class user(models.Model):
#     Uname=models.CharField()
#     Umail=models.CharField()
#     image=models.CharField()
    