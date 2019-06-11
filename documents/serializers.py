from rest_framework import serializers
from .models import Document
from demands.models import Demand
from users.serializers import UserSerializer
from demands.serializers import DemandSerializer


class DocumentSerializer(serializers.ModelSerializer):
    date_create = serializers.ReadOnlyField()
    user_create = UserSerializer(read_only=True)
    demand = serializers.PrimaryKeyRelatedField(write_only=False,
                                               queryset=Demand.objects.all())

    class Meta:
        model = Document
        fields = (
            'date_create',
            'user_create',
            'demand',
            'name_doc',
            'url',
        )