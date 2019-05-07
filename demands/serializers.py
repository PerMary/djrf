from rest_framework import serializers
from .models import Demand, Position
from django.utils import timezone
from django.contrib.auth.models import User
from users.serializers import UserSerializer, ProfileSerializer



class PositionSerializer(serializers.ModelSerializer):
    demand = serializers.PrimaryKeyRelatedField(write_only=False,
                                               queryset=Demand.objects.all())

    class Meta:
        model = Position
        fields = (
            'id',
            'demand',
            'name_product',
            'art_product',
            'quantity',
            'price_one',)


class DemandSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_date = serializers.ReadOnlyField()
    #positions = serializers.PrimaryKeyRelatedField(many=True,queryset=Position.objects.all())
    positions = PositionSerializer(read_only=True,)
                                   #queryset=Position.objects.filter(demand=1))

    class Meta:
        model = Demand
        fields = (
            'id',
            'created_date',
            'description',
            'user',
            'positions') #Как сделать, чтобы для каждой завки выводились ее позиции

        # def create(self, validated_data):
        #     position_data = validated_data.pop('position')
        #     #demand = Demand.objects.create_demand(**validated_data)
        #     demand =Demand.objects.create_demand(**validated_data)
        #     Position.object.create(position=position, **position_data)
        #     return demand


# class UserSerializer(serializers.ModelSerializer):
#     #demands = serializers.PrimaryKeyRelatedField(many=True, queryset=Demand.objects.all())
#
#
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',) #Если оставить demands и добавить его здесь, то будет видно какие заявки пользователь создал

