# Generated by Django 4.2.4 on 2023-08-21 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_deadline_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 22, 34, 36, 578413)),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 22, 34, 36, 578413)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 22, 34, 36, 577416)),
        ),
    ]