# Generated by Django 2.2.3 on 2019-08-01 03:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateField(default=datetime.datetime(2019, 8, 1, 3, 25, 13, 783162, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateField(default=datetime.datetime(2019, 8, 1, 3, 25, 13, 783187, tzinfo=utc)),
        ),
    ]
