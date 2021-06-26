from django.db import models

# Create your models here.

class GeneralRegistration(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)
    gender = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class StudentRegistration(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    level = models.PositiveIntegerField()
    interest = models.CharField(max_length=250)


    def __str__(self):
        return self.email


class EmployerRegistration(models.Model):
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    business_name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    address = models.TextField()
    

    def __str__(self):
        return self.business_name + ' ' + self.email