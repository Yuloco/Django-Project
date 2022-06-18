from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class post(models.Model):
    Text=models.TextField()
    Title=models.CharField(max_length=200)
    Author=models.ForeignKey(get_user_model)
    Created_date=models.DateTimeField()
    Publish_date=models.DateTimeField()
