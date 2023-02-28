from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile, User
from .serializers import UserBasicsSerializer, UserDetailsSerializer


@api_view(['POST', ])
def search_user(request):
    max_age = request.data['max_age']
    min_age = request.data['min_age']
    hometown = request.data['hometown']
    gander = request.data['gander']

    profile_list = Profile.objects.filter(hometown__contains=hometown)

    if gander:
        profile_list = profile_list.filter(gander=gander)

    if max_age:
        profile_list = profile_list.filter(age__lte=max_age)

    if min_age:
        profile_list = profile_list.filter(age__gte=min_age)

    users_list = []
    for profile in profile_list:
        user = User.objects.get(profile=profile)
        serializer = UserBasicsSerializer(user)
        users_list.append(serializer.data)

    return Response(users_list, status=200)


@api_view(['GET'])
def get_user_by_id(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserDetailsSerializer(user)
    return Response(serializer.data, status=200)
