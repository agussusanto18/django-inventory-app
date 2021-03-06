# Generated by Django 3.2 on 2021-08-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0003_auto_20210821_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='provider',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='itemreservation',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
