# Generated by Django 3.2 on 2022-01-31 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220131_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_user',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.date(2022, 2, 1)),
        ),
    ]
