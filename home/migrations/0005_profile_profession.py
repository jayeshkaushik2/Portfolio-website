# Generated by Django 3.2 on 2022-01-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220201_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.TextField(null=True),
        ),
    ]