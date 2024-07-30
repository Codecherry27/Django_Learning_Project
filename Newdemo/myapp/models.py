from django.db import models

# Create your models here.
class createnew(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    