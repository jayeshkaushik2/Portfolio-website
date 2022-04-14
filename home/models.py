from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(null=False)
    post_title = models.TextField(null=False)
    post_description = models.TextField(null=True)
    post_date = models.DateField(default=date.today())

    def __str__(self):
        return self.post_title[0:50]

class Profile(models.Model):
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True)
    backprofile_image = models.ImageField(blank=True)
    about_user = models.TextField(null=True)
    profession = models.CharField(null=True, max_length=255)

class SocialLink(models.Model):
    sociallink_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.CharField(null=True, max_length=600)
    linkedin = models.CharField(null=True, max_length=600)
    github = models.CharField(null=True, max_length=600)
    coding = models.CharField(null=True, max_length=600)

class Education(models.Model):
    school_name = models.CharField(null=False, max_length=200)
    course_name = models.CharField(null=False, max_length=200)
    stream_name = models.CharField(null=False, max_length=200)
    start = models.DateField()
    end = models.DateField()
    marks = models.FloatField()