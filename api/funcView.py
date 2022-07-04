from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
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
    elif request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user
            if "school" in request.data or "course" in request.data:
                edu = Education.objects.filter(user=user_id, school=request.data["school"], course=request.data["course"]).first()
            if edu is None:
                edu = Education.objects.create(user=user_id)
            sz = EducationSz(instance=edu, data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    else:
        if request.user.is_authenticated:
            breakpoint()
            return Response({"status":204})


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
        if request.user.is_authenticated:
            user_id = request.user
            experience = Experience.objects.create(user=user_id)
            sz = ExperienceSz(instance=experience, data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    else:
        pass


@api_view(['GET'])
def getPost(request, pk):
    '''
    1. getting a specific post using its id.
    2. since we want only one post so --> many=False
    '''
    post = Post.objects.get(id=pk)
    serializer = PostSz(post, many=False)
    return Response(serializer.data)


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
        if request.user.is_authenticated:
            user_id = request.user
            skill = Skill.objects.create(user=user_id)
            sz = SkillSz(instance=skill, data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
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
        if request.user.is_authenticated:
            user_id = request.user
            project = Project.objects.create(user=user_id)
            sz = ProjectSz(instance=project, data=request.data, partial=True)
            if sz.is_valid(raise_exception=True):
                sz.save()
                return Response(sz.data)
        return Response({"error":"Unable to update Data"}, status=401)
    else:
        pass