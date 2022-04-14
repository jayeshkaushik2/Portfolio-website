from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import PostSerializer, ProfileSerializer
from home.models import Post, Profile


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
        user_id = request.user.id
        print(type(user_id))
    except Exception as e:
        print(e)
        pass

    profile = Profile.objects.get(profile_user=1)
    print(profile)
    serializer = ProfileSerializer(profile, many=False)

    return Response(serializer.data)