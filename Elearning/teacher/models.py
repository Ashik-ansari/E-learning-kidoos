from django.db import models
from admin1.models import *

# Create your models here.

class Tutorial(models.Model):
    standard = models.ForeignKey(Myclass,on_delete = models.CASCADE)
    chapter=models.CharField(max_length=255,null=False)
    description=models.CharField(max_length=255,null=False)
    video=models.FileField(upload_to='media/',null=True)
    subject=models.CharField(max_length=255,null=False)

    def videourl1(self):
        if self.video == '':
            video =''
        else:
            video = self.video.url
        return video        