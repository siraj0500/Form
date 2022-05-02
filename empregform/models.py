from django.db import models


# Create your models here.

class Form(models.Model):
    # job role choices
    CHOICES1 = (
        ('frontend_developer', 'frontend_developer'),
        ('php_developer', 'php_developer'),
        ('Python_Developer', 'Python_Developer'),
        ('Rails_Developer', 'Rails_Developer'),
        ('Web_Designer', 'Web_Designer'),
        ('WordPress_Developer', 'WordPress_Developer'),
        ('Android_Developer', 'Android_Developer'),
        ('iOS_Developer', 'iOS_Developer'),
        ('Mobile_Designer', 'Mobile_Designer'),
        ('Business_Owner', 'Business_Owner'),
        ('Freelancer', 'Freelancer'),
        ('Secretary', 'Secretary'),
        ('Maintenance', 'Maintenance')
    )
    CHOICES2 = (
        ('Development', 'Development'),
        ('Design', 'Design'),
        ('Business', 'Business')
    )

    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500)
    j_role = models.CharField(max_length=500, choices=CHOICES1)
    interests = models.CharField(max_length=500, choices=CHOICES2)

    def __str__(self):
        return self.name