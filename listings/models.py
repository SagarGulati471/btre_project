from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here


class Listing(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField()
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    photo_main=models.ImageField(upload_to="photos/%Y/%m/%d")
    photo1=models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo2=models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo3=models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo4=models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo5=models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    is_published=models.BooleanField()
    list_date=models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.title




