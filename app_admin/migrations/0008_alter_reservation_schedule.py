# Generated by Django 3.2 on 2021-08-27 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0007_alter_reservation_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='schedule',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
