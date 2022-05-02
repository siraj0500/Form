from django.contrib import admin
from .models import Contact


class Contactadmin(admin.ModelAdmin):
    list_display = ('usn', 'name', 'sem', 'phone', 'email','pic')


# Register your models here.
admin.site.register(Contact,Contactadmin)
