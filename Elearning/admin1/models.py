from django.db import models

# Create your models here.

class Myclass(models.Model):
    standard = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=10)
    sub1=models.CharField(max_length=50)
    sub2=models.CharField(max_length=50)
    sub3=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/',null=True)
    video=models.FileField(upload_to='media/',null=True)

    @property
    def imgurl5(self):
        if self.image == '':
            image =''
        else:
            image = self.image.url
        return image    

    def videourl(self):
        if self.video == '':
            video =''
        else:
            video = self.video.url
        return video        

class Teachers(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile_number=models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    experience =models.CharField(max_length=255)
    standard = models.ForeignKey(Myclass,on_delete = models.CASCADE)
    active = models.BooleanField(default=True)
    username = models.CharField(max_length=255,null=False)
    password = models.CharField(max_length=255,null=False)
    confirm_password=models.CharField(max_length=255,null=False)
    image=models.ImageField(upload_to='media/',null=True)
    date = models.DateField(auto_now_add=True, null=True)

    @property
    def imgurl4(self):
        if self.image == '':
            image =''
        else:
            image = self.image.url
        return image    
