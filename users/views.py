from rest_framework import viewsets
from users.serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from users.models import Profile

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
