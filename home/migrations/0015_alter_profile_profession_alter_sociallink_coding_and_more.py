# Generated by Django 4.0.4 on 2022-06-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='coding',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='email',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='github',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='linkedin',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]