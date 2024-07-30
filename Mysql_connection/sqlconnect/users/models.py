from django.db import models

# Create your models here.
class us(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)

class person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)