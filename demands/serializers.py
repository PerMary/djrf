from rest_framework import serializers
from .models import Demand, Position
from django.utils import timezone
#from django.contrib.auth.models import User
from users.serializers import UserSerializer



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
            'price_one',
            'full_price_position', )


class DemandSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_date = serializers.ReadOnlyField()
    # positions = PositionSerializer(read_only=True,
    #                                many=True)
    # positions_id = serializers.PrimaryKeyRelatedField(read_only=True,
    #                                                   many=True,
    #                                                   source='positions',
    #                                                   queryset=Position.objects.all())

    class Meta:
        model = Demand
        fields = (
            'id',
            'created_date',
            'description',
            'user',
            # 'positions',
            'position_count',
            'product_count',
            'price_all'
        )

# class DemandPosSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     created_date = serializers.ReadOnlyField()
#     positions = PositionSerializer(read_only=True,
#                                    many=True)
    # positions_id = serializers.PrimaryKeyRelatedField(read_only=True,
    #                                                   many=True,
    #                                                   source='positions',)
    #                                                   # queryset=Position.objects.all() )
    #
    # class Meta:
    #     model=Demand
    #     fields = (
    #         'id',
    #         'created_date',
    #         'description',
    #         'user',
    #         'positions',
    #         'position_count',
    #         'product_count',
    #         'price_all'
    #     )
