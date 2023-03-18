from django.db import models

# Create your models here.

class RatingModel(models.Model):
    avgrating:str
    behaviour:int
    toiletcleanliness:int
    inhousestay:bool
    disableperson_friendly:bool
    medical_emergency:bool
    food_facility:int
    about:str
    