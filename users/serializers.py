from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile

class UserSerializer(serializers.ModelSerializer):
    #demands = serializers.PrimaryKeyRelatedField(many=True, queryset=Demand.objects.all())


    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
        ) #Если оставить demands и добавить его здесь, то будет видно какие заявки пользователь создал


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(write_only=True,
                                              source='users',
                                              queryset=User.objects.all(),)


    class Meta:
        model = Profile
        fields = (
            'user',
            'firstname',
            'lastname',
            'middle_name',
        )
