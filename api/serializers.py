from dataclasses import field
from rest_framework.serializers import ModelSerializer

from home.models import Post, Profile, SocialLink


class PostSz(ModelSerializer):
    class Meta:
        model = Post
        # here fields can added as a list --> ['name', 'lastname', 'fields name'] or if you want to add all fields then you can you --> '__all__'
        fields = "__all__"


class ProfileSz(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "profile_image",
            "backprofile_image",
            "about_user",
            "profession",
        ]


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
