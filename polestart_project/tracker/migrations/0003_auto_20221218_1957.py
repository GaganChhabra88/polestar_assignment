# Generated by Django 3.2 on 2022-12-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_vessel_vessel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vessel',
            name='create_datetime',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='update_datetime',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
