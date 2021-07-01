#from Elearning import student
from admin1.models import Myclass
from django.db import models
from django.contrib.auth.models import User

from admin1.models import *
# Create your models here.



class Students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255,null=False)    
    parent_name = models.CharField(max_length=255,null=False)
    student_age = models.IntegerField(default=0,null=False)
    mobile_number = models.CharField(max_length=255,null=False)
    standard = models.ForeignKey(Myclass,on_delete = models.CASCADE,null=True)
    price = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True)
    image=models.ImageField(upload_to='media/',null=True)

    @property
    def imgurl4(self):
        if self.image == '':
            image =''
        else:
            image = self.image.url
        return image


class Order(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    standard=models.ForeignKey(Myclass, on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    status=models.CharField(max_length=50)
    payment_method=models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
   
    
    
