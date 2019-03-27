from rest_framework import serializers
from .models import Demand, Position
from django.utils import timezone
from django.contrib.auth.models import User


class DemandSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    created_date = serializers.ReadOnlyField()


    class Meta:
        model = Demand
        fields = ('id', 'created_date', 'description', 'user')




class PositionSerializer(serializers.ModelSerializer):
    demands = DemandSerializer(read_only=True)
    id_demand = serializers.PrimaryKeyRelatedField(write_only=True, source='demands', queryset=Demand.objects.all())

    class Meta:
        model = Position
        fields = ('id','demands', 'id_demand', 'name_product', 'art_product', 'quantity', 'price_one')


class UserSerializer(serializers.ModelSerializer):
    demands = serializers.PrimaryKeyRelatedField(many=True, queryset=Demand.objects.all())


    class Meta:
        model = User
        fields = ('id', 'username', 'demands')
