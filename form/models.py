from django.db import models


# Create your models here.
class Contact(models.Model):
    usn = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='')
    name = models.CharField(max_length=50, default="")
    sem = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=13, default="")
    email = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name
