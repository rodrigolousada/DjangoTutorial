# Generated by Django 2.2.3 on 2019-07-15 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 15, 11, 0, 872782), verbose_name='Date published'),
        ),
    ]
