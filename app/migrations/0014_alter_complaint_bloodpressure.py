# Generated by Django 4.0.6 on 2022-10-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220828_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='bloodPressure',
            field=models.CharField(max_length=100),
        ),
    ]
