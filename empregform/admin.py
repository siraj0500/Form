from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'birthday', 'bio', 'j_role', 'interests')


# Register your models here.
admin.site.register(Form, FormAdmin)
