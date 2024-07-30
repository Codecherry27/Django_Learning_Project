from django.db import models

# Create your models here.

class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type_of_company=models.CharField(max_length=50,choices=(('IT','IT'),('NonIT','NonIT'),('Mobile','Mobile')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name+"("+self.location+")"

class employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('Manager','Manager'),('Developer','Developer'),('Team Lead','Team Lead')))

    Company = models.ForeignKey(company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
