from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import viewsets
from home.models import Education, Experience, Post, Profile, Project, Skill, SocialLink
from .serializers import PostSz, ProfileSz, SocialLinkSz, EducationSz, ExperienceSz, SkillSz, ProjectSz


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


class Getpost(viewsets.ModelViewSet):
    '''
    1. getting all the posts from the database.
    2. serializing the data for the json response.
    3. Now we have to get the data from serialized format (serializer.data)

    Note: "many" --> this specifies if it should converts a single object(when false) or multiple objects(when true)
    '''
    serializer_class = PostSz
    def get_queryset(self):
        posts = Post.objects.all()
        return posts
    
    def perform_create(self, serializer):
        post = Post.objects.create(user=User.objects.all()[0])
        serializer.save(instance=post)

@api_view(['GET'])
def getPost(request, pk):
    '''
    1. getting a specific post using its id.
    2. since we want only one post so --> many=False
    '''
    post = Post.objects.get(id=pk)
    serializer = PostSz(post, many=False)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getProfile(request):
    '''
    This will give us the profile image of the user
    '''
    if request.method == "GET":
        user_id = 1
        try:
            print("trying to get user id...")
            user_id = request.user.id
            print(user_id)
        except Exception as e:
            print("Failed to get user id...")
            pass
        
        if user_id is None:
            user_id = 1

        profile = Profile.objects.get(user=user_id)
        serializer = ProfileSz(profile, many=False)

        return Response(serializer.data)
    else:
        user_id = 1
        breakpoint()
        profile, created = Profile.objects.get_or_create(user=user_id)
        sz = ProfileSz(instance=profile, data=request.data, partial=True)
        if sz.is_valid(raise_exception=True):
            sz.save()
            return Response(sz.data)
        return Response({"success":False})

@api_view(['GET', 'POST'])
def getSocialLink(request):
    if request.method == "GET":
        user_id = 1
        try:
            user_id = request.user.id
        except Exception as e:
            print("failed to get user id...")
            pass
        if user_id is None:
            user_id = 1
        social_links = SocialLink.objects.get(user=user_id)
        sz = SocialLinkSz(instance=social_links, many=False)
        return Response(sz.data)
    else:
        user_id = 1
        sociallinks = SocialLink.objects.get(user=user_id)
        sz = SocialLinkSz(instance=sociallinks, data=request.data, partial=True)
        if sz.is_valid(raise_exception=True):
            sz.save()
            return Response(sz.data)
        return Response({"success":False})

@api_view(['GET', 'POST'])
def getEducation(request):
    if request.method == 'GET':
        user_id = 1
        try:
            user_id = request.user.id
        except Exception as e:
            print("Failed to get the user id...")
            pass
        if user_id is None:
            user_id = 1
        education_details = Education.objects.filter(user=user_id)
        sz = EducationSz(instance=education_details, many=True)
        return Response(sz.data)
    else:
        user_id = 1
        if "school" in request.data or "course" in request.data:
            edu = Education.objects.filter(user=user_id, school=request.data["school"], course=request.data["course"]).first()
        if edu is None:
            edu = Education.objects.create(user=User.objects.all()[0])
        sz = EducationSz(instance=edu, data=request.data, partial=True)
        if sz.is_valid(raise_exception=True):
            sz.save()
            return Response(sz.data)
        return Response({"success":False})


@api_view(['GET', 'POST', 'DELETE'])
def getExperience(request):
    if request.method == 'GET':
        user_id = 1
        try:
            user_id = request.user.id
        except Exception as e:
            print("Failed to get the user id...")
            pass
        
        if user_id is None:
            user_id = 1
        
        experience_details = Experience.objects.filter(user=user_id)
        sz = ExperienceSz(instance=experience_details, many=True)
        
        return Response(sz.data)
    elif request.method == 'POST':
        user_id = 1
        experience = Experience.objects.create(user=User.objects.all()[0])
        sz = ExperienceSz(instance=experience, data=request.data, partial=True)
        if sz.is_valid(raise_exception=True):
            sz.save()
            return Response(sz.data)
    else:
        pass


@api_view(['GET', 'POST', 'DELETE'])
def getSkill(request):
    if request.method == 'GET':
        user_id = 1
        try:
            user_id = request.user.id
        except Exception as e:
            print("Failed to get the user id...")
            pass
        if user_id is None:
            user_id = 1
        skill_details = Skill.objects.filter(user=user_id)
        sz = SkillSz(instance=skill_details, many=True)
        return Response(sz.data)
    elif request.method == 'POST':
        user_id = 1
        skill = Skill.objects.create(user=User.objects.all()[0])
        sz = SkillSz(instance=skill, data=request.data, partial=True)
        if sz.is_valid(raise_exception=True):
            sz.save()
            return Response(sz.data)
    else:
        pass

@api_view(['GET', 'POST', 'DELETE'])
def getProject(request):
    if request.method == 'GET':
        user_id = 1
        try:
            user_id = request.user.id
        except Exception as e:
            print("Failed to get the user id...")
            pass
        if user_id is None:
            user_id = 1
        project_details = Project.objects.filter(user=user_id)
        sz = ProjectSz(instance=project_details, many=True)
        return Response(sz.data)
    elif request.method == 'POST':
        user_id = 1
        project = Project.objects.create(user=User.objects.all()[0])
        sz = ProjectSz(instance=project, data=request.data, partial=True)
        if sz.is_valid(raise_exception=True):
            sz.save()
            return Response(sz.data)
    else:
        pass