from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.

class Vessel(models.Model):
    id = models.AutoField(primary_key=True, editable=False) 
    imo_number = models.IntegerField(blank=False,null=False)
    vessel_name = models.CharField(max_length=500,blank=True,null=True)		
    timestamp = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)],)
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)],) 
    created_by = models.IntegerField(blank=True, null=True,default=1) # to be referenced from the user model	
    create_datetime = models.DateField(auto_now_add=True,blank=True,null=True)		
    update_datetime = models.DateField(auto_now=True,blank=True,null=True)		
    
    class Meta:
        db_table = "vessel"


    def __str__(self):
        return self.vessel_name
