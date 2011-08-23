from django.db import models

class KV(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=True)
    meta = models.CharField(max_length=100,blank=True,null=True)
    ref = models.ForeignKey('self',blank=True,null=True)

# Create your models here.
