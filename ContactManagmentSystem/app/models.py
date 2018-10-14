"""
Definition of models.
"""

from django.db import models

PHONE_CHOICES=(('Phone Type','Phone Type'),('Home','Home'),('Work','Work'),('Cell','Cell'),('Other','Other'))


# Create your models here.
class Contacts(models.Model):
    Fname=models.CharField(max_length=20,null=True)
    Mname=models.CharField(max_length=20,null=True)
    Lname=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.Fname +" " + self.Lname

class Date (models.Model):
    Contact_id=models.ForeignKey(Contacts,on_delete=models.CASCADE,related_name='dates')
    Date_type=models.CharField(max_length=30,null=True)
    Date=models.DateTimeField(null=True)

class Phone(models.Model):
    Contact_id=models.ForeignKey(Contacts,on_delete=models.CASCADE,related_name='phones')
    Phone_type=models.CharField(max_length=30, choices=PHONE_CHOICES, null=True)
    Area_code=models.CharField(max_length=3,null=True)
    Number=models.CharField(max_length=8,null=True)

class Address(models.Model):
    Contact_id=models.ForeignKey(Contacts,on_delete=models.CASCADE,related_name='addresses')
    Address_type=models.CharField(max_length=30,null=True)
    Address=models.CharField(max_length=200,null=True)
    City=models.CharField(max_length=20,null=True)
    State=models.CharField(max_length=20,null=True)
    Zip=models.CharField(max_length=5,null=True)
