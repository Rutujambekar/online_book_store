from django.db import models

# Create your models here.

class StoreInfo(models.Model):
    username=models.CharField(max_length=50)
    storename=models.CharField(max_length=50)
    totalbooks=models.IntegerField(default=0)
    storeimage=models.ImageField(null=True, blank=True)
    rating=models.FloatField(default=4.5)
    first_name=models.CharField(max_length=50, default='abc')
    last_name=models.CharField(max_length=50, default='xyz')

    class Meta:
        db_table='storeinfo'


class BookInfo(models.Model):
    bookid=models.CharField(max_length=50, primary_key=True)
    username=models.CharField(max_length=50)
    storename=models.CharField(max_length=50)
    bookname=models.CharField(max_length=50)
    bookprice=models.IntegerField(default=1)
    bookauthor=models.CharField(max_length=50)
    bookimage=models.ImageField(null=True, blank=True)

    class Meta:
        db_table='bookinfo'
    