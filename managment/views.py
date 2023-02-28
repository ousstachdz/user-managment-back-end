from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile, User
from .serializers import UserSerializer


@api_view(['GET', 'POST', ])
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
        serializer = UserSerializer(user)
        users_list.append(serializer.data)

    return Response(users_list, status=200)
