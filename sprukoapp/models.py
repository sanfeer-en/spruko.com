from django.db import models

# Create your models here.
class UserDeatils(models.Model):
    username=models.CharField(max_length=250)
    passwords=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.IntegerField()
    birth=models.DateField()
    
    def __str__(self):
        return self.username
    
