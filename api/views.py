from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import PostSerializer, ProfileSerializer
from home.models import Post, Profile
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def admin_login(request, pk):
    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        if user is None:
            return HttpResponse("user is None...")
        if user.is_authenticated:
            print(f"user {user} is logged in...")
            profile = Profile.objects.filter(user=user).first()
            sz = ProfileSerializer(instance=profile)
            return Response(sz.data)
        else:
            return Response({})
    else:
        return HttpResponse("This is post")


@api_view(['GET'])
def getPosts(request):
    '''
    1. getting all the posts from the database.
    2. serializing the data for the json response.
    3. Now we have to get the data from serialized format (serializer.data)

    Note: "many" --> this specifies if it should converts a single object(when false) or multiple objects(when true)
    '''

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getPost(request, pk):
    '''
    1. getting a specific post using its id.
    2. since we want only one post so --> many=False
    '''
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def getProfile(request):
    '''
    This will give us the profile image of the user
    '''
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
    serializer = ProfileSerializer(profile, many=False)

    return Response(serializer.data)