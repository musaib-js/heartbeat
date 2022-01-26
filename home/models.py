from tabnanny import verbose
from django.db import models

# Create your models here.
class donation_plea(models.Model):
    sno = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=13)
    requirement = models.CharField(max_length = 250)
    birth_date = models.IntegerField()
    birth_month = models.CharField(max_length=2)
    birth_year = models.CharField(max_length=4)
    message = models.TextField()

    def __str__(self):
        return "Donation Plea By " +  self.full_name

    class Meta:
        verbose_name_plural = "Donation Pleas"

# Model for donations
class donation(models.Model):
    sno  = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=13)
    organ = models.CharField(max_length = 250)
    birth_date = models.IntegerField()
    birth_month = models.CharField(max_length=2)
    birth_year = models.CharField(max_length=4)
    message = models.TextField()

    def __str__(self):
        return "Donation of " + self.organ + " by " + self.full_name
    