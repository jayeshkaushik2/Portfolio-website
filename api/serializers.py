from dataclasses import field
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from home.models import Education, Experience, Post, Profile, Project, Skill, SocialLink
from drf_extra_fields.fields import Base64ImageField

class PostSz(ModelSerializer):
    post_image = serializers.ImageField(required=False)
    class Meta:
        model = Post
        # here fields can added as a list --> ['name', 'lastname', 'fields name'] or if you want to add all fields then you can you --> '__all__'
        fields = "__all__"


class ProfileSz(ModelSerializer):
    total_posts = serializers.SerializerMethodField()
    total_projects = serializers.SerializerMethodField()
    total_certificates = serializers.SerializerMethodField()
    profile_image = serializers.ImageField(required=False)
    backprofile_image = serializers.ImageField(required=False)
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "name",
            "profile_image",
            "backprofile_image",
            "about_user",
            "profession",
            "total_posts",
            "total_projects",
            "total_certificates",
        ]

    def get_total_posts(self, obj):
        return len(Post.objects.all())
    
    def get_total_projects(self, obj):
        return len(Project.objects.all())

    def get_total_certificates(self, obj):
        return 0

class SocialLinkSz(ModelSerializer):
    class Meta:
        model = SocialLink
        fields = [
            "id",
            "user",
            "email",
            "linkedin",
            "github",
            "coding",
        ]

class EducationSz(ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id",
            "user",
            "school",
            "course",
            "stream",
            "start",
            "end",
            "marks",
        ]

class ExperienceSz(ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "user",
            "position",
            "company",
            "type",
            "start",
            "end",
            "is_active",
        ]

class SkillSz(ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "user",
            "skill_name",
        ]

class ProjectSz(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "user",
            "title",
            "description",
            "link",
            "start",
            "end",
            "is_active",
        ]