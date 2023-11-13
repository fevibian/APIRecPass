from django.db import models

# Create your models here.

class Newpass(models.Model):
    email = models.EmailField(max_length=100,unique = True)
    password = models.CharField(max_length=50,default='DEFAULT VALUE')

    class Meta:
        db_table = 'newpass'
    
    def __str__(self):
        return self.nombre
