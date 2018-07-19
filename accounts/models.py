from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class OtherInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    mob=models.BigIntegerField()



def  __str__(self):
    return self.title
