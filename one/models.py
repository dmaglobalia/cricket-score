from django.db import models

# Create your models here.

class score(models.Model):
    team_name = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    wicket = models.IntegerField()
    vs = models.CharField(max_length=255)

    
    score2 = models.CharField(max_length=255,null=True,blank=True)
    wicket2 = models.IntegerField(null=True,blank=True)
    
    logo = models.ImageField(upload_to='images',null=True,blank=True)