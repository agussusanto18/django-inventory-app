# Generated by Django 3.2 on 2021-08-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0004_auto_20210822_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
