from rest_framework import serializers
from .models import Demand, Position
from django.utils import timezone
from django.contrib.auth.models import User


class DemandSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    created_date = serializers.ReadOnlyField()
    positions = serializers.PrimaryKeyRelatedField( read_only=True)


    class Meta:
        model = Demand
        fields = (
            'id',
            'created_date',
            'description',
            'user',
            'positions',)




class PositionSerializer(serializers.ModelSerializer):
    id_demand = serializers.PrimaryKeyRelatedField( queryset=Demand.objects.all())

    class Meta:
        model = Position
        fields = (
            'id',
            'id_demand',
            'name_product',
            'art_product',
            'quantity',
            'price_one',)


class UserSerializer(serializers.ModelSerializer):
    #demands = serializers.PrimaryKeyRelatedField(many=True, queryset=Demand.objects.all())


    class Meta:
        model = User
        fields = (
            'id',
            'username',) #Если оставить demands и добавить его здесь, то убдет видно какие заявки пользователь создал
