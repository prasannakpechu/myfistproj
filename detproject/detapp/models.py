from django.db import models

# Create your models here.

class detemployee(models.Model):
    age = models.CharField(max_length=50,null=True,blank = True)
    work = models.CharField(max_length=50,null=True,blank = True)
    fwt = models.CharField(max_length=50,null=True,blank = True)
    education = models.CharField(max_length=50,null=True,blank = True)
    edu_no = models.CharField(max_length=50,null=True,blank = True)
    marital_status = models.CharField(max_length=50,null=True,blank = True)
    occupation = models.CharField(max_length=50,null=True,blank = True)
    relationship = models.CharField(max_length=50,null=True,blank = True)
    race = models.CharField(max_length=50,null=True,blank = True)
    sex = models.CharField(max_length=50,null=True,blank = True)
    cap_gain = models.CharField(max_length=50,null=True,blank = True)
    cap_loss = models.CharField(max_length=50,null=True,blank = True)
    hours_pw = models.CharField(max_length=50,null=True,blank = True)
    native_country = models.CharField(max_length=50,null=True,blank = True)
    salary = models.TextField(null=True,blank = True)
