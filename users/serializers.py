from rest_framework import serializers
#from django.contrib.auth.models import User
#from users.models import Profile
from demands.models import Demand
from django.contrib.auth import get_user_model
#from demands.serializers import DemandSerializer #Поооооочееееемуууууу не могу импортировать




User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    #demands = serializers.PrimaryKeyRelatedField(many=True, queryset=Demand.objects.all())
    #demands = DemandSerializer(read_only=True) #очему не могу импортировать DemandSerializer&

    class Meta:
        model = User
        # ref_name = 'custom_user'
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'full_name',
            'short_name',
            #'demands', #вывод заявок которые пользовтель создал
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    #Как сделать обновление пароля, чтобы он не был хэшем если его не изменять / Djoser
    def update(self, instance, validated_data):
        print(validated_data)
        instance.username=validated_data.get('username', instance.username)
        instance.email=validated_data.get('email', instance.email)
        instance.first_name=validated_data.get('first_name', instance.first_name)
        instance.last_name=validated_data.get('last_name', instance.last_name)
        instance.middle_name=validated_data.get('middle_name', instance.middle_name)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance

