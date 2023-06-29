from django.db import models

# Create your models here.
class Food(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    isbn=models.CharField(max_length=15)
    bookname=models.CharField(max_length=10)
    publishertime=models.CharField(max_length=20)