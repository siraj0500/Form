# Generated by Django 4.0.3 on 2022-03-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregform', '0002_remove_form_picture_alter_form_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
