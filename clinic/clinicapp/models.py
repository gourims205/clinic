from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    department=models.CharField(max_length=100)
    date = models.DateField()
    doctor = models.CharField(max_length=50)
    message= models.CharField(max_length=200, blank=True,null=True)

    def __str__(self):
        return self.name
    