# Generated by Django 3.1.7 on 2021-04-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0006_auto_20210401_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollutant',
            name='color',
            field=models.CharField(default='#000000', max_length=30),
        ),
    ]
