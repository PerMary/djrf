from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # #user = serializers.PrimaryKeyRelatedField(read_only=True,
    #                                           source='users',
    #                                           )


    class Meta:
        model = Profile
        fields = (
            'firstname',
            'lastname',
            'middle_name',
        )


class UserSerializer(serializers.ModelSerializer):
    #demands = serializers.PrimaryKeyRelatedField(many=True, queryset=Demand.objects.all())
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'profile',
        ) #Если оставить demands и добавить его здесь, то будет видно какие заявки пользователь создал

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

