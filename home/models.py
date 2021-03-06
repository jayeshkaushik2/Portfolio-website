from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(null=False)
    post_title = models.TextField(null=False)
    post_description = models.TextField(null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title[0:50]

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=256, null=True, blank=True)
    profile_image = models.ImageField(blank=True, null=True)
    backprofile_image = models.ImageField(blank=True, null=True)
    about_user = models.TextField(null=True)
    profession = models.CharField(null=True, max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.CharField(null=True, max_length=600, blank=True)
    linkedin = models.CharField(null=True, max_length=600, blank=True)
    github = models.CharField(null=True, max_length=600, blank=True)
    coding = models.CharField(null=True, max_length=600, blank=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(null=False, max_length=200)
    course = models.CharField(null=False, max_length=200)
    stream = models.CharField(null=False, max_length=200)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    marks = models.FloatField(null=True)
    
    def __str__(self):
        return self.school

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=256, null=True, blank=True)
    company = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.company

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.skill_name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=256, null=True, blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title