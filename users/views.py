from rest_framework import viewsets
from users.serializers import UserSerializer
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#from users.models import Profile
from django.conf import settings
from rest_framework import permissions
from demands.permissions import IsOwnerOrReadOnly
#settings.AUTH_USER_MODEL as User


User=get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #                      IsOwnerOrReadOnly,)



#class ProfileViewSet(viewsets.ModelViewSet):
    # queryset = Profile.objects.all()
    # serializer_class = ProfileSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # #                      IsOwnerOrReadOnly,)