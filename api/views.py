from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import viewsets
from home.models import Education, Experience, Post, Profile, Project, Skill, SocialLink
from .serializers import PostSz, ProfileSz, SocialLinkSz, EducationSz, ExperienceSz, SkillSz, ProjectSz
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST'])
def admin_login(request, pk):
    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        if user is None:
            return HttpResponse("user is None...")
        if user.is_authenticated:
            print(f"user {user} is logged in...")
            profile = Profile.objects.filter(user=user).first()
            sz = ProfileSz(instance=profile)
            return Response(sz.data)
        else:
            return Response({})
    else:
        return HttpResponse("This is post")

from rest_framework.parsers import MultiPartParser, FileUploadParser

class Getpost(viewsets.ModelViewSet):
    serializer_class = PostSz
    parser_classes = (MultiPartParser, FileUploadParser)

    def get_queryset(self):
        posts = Post.objects.all().order_by("-id")
        return posts
    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = self.request.user
            request.data["user"] = user_id.id
            sz = self.serializer_class(data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    
    def perform_create(self, serializer):
        serializer.save(data=self.request.data)


@api_view(['GET', 'POST'])
def getProfile(request):
    '''
    This will give us the profile image of the user
    '''
    if request.method == "GET":
        profile = Profile.objects.all().first()
        serializer = ProfileSz(profile, many=False)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            user_id = request.user
            profile, created = Profile.objects.get_or_create(user=user_id)
            sz = ProfileSz(instance=profile, data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)


@api_view(['GET', 'POST'])
def getSocialLink(request):
    if request.method == "GET":
        social_links = SocialLink.objects.all().first()
        sz = SocialLinkSz(instance=social_links, many=False)
        return Response(sz.data)
    else:
        if request.user.is_authenticated:
            user_id = request.user
            sociallinks = SocialLink.objects.get(user=user_id)
            sz = SocialLinkSz(instance=sociallinks, data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)


class EducationApi(viewsets.ModelViewSet):
    serializer_class = EducationSz
    def get_queryset(self):
        educations = Education.objects.all()
        return educations
    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = self.request.user
            request.data["user"] = user_id.id
            sz = self.serializer_class(data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    
    def perform_create(self, serializer):
        serializer.save(data=self.request.data)


class ExperienceApi(viewsets.ModelViewSet):
    serializer_class = ExperienceSz
    def get_queryset(self):
        experiences = Experience.objects.all()
        return experiences

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = self.request.user
            request.data["user"] = user_id.id
            sz = self.serializer_class(data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    
    def perform_create(self, serializer):
        serializer.save(data=self.request.data)


class SkillApi(viewsets.ModelViewSet):
    serializer_class = SkillSz
    def get_queryset(self):
        skills = Skill.objects.all()
        return skills
    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = self.request.user
            request.data["user"] = user_id.id
            sz = self.serializer_class(data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    
    def perform_create(self, serializer):
        serializer.save(data=self.request.data)


class ProjectApi(viewsets.ModelViewSet):
    serializer_class = ProjectSz
    def get_queryset(self):
        projects = Project.objects.all()
        return projects
    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = self.request.user
            request.data["user"] = user_id.id
            sz = self.serializer_class(data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    
    def perform_create(self, serializer):
        serializer.save(data=self.request.data)
