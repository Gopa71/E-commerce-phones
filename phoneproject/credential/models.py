from django.db import models

# Create your models here.
class Credential(models.Model):
    username=models.CharField(max_length=250,unique=True)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)
    compassword=models.CharField(max_length=250)

    def __str__(self):      
        return '{}'.format(self.username)