from .models import Demand, Position
from demands.serializers import DemandSerializer, PositionSerializer, DemandPosSerializer
from rest_framework import generics
#from django.contrib.auth.models import User
from rest_framework import permissions
from demands.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404





class DemandViewSet(viewsets.ViewSet):
    # queryset = Demand.objects.all()
    # serializer_class = DemandSerializer


    def list(self, request, *args, **kwargs):
        queryset = Demand.objects.all()
        seriaizer = DemandSerializer(queryset, many=True)
        return Response (seriaizer.data)

    def retrieve(self, request, pk=None):
        queryset = Demand.objects.all()
        demand = get_object_or_404(queryset, pk=pk)
        seriaizer = DemandPosSerializer(demand)
        return Response(seriaizer.data)
    # эта штука в список выводит все заявки заявки без позиций, но если перейти к
    # конкретной заявке /id то там будет описание заявки и плюс ее позиции



    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #                       IsOwnerOrReadOnly,)

    # @action(
    #   detail=True,
    #   renderer_classes=[renderers.StaticHTMLRenderer],
    #   )
    # def highlight(self, request,):
    #    demand = self.get_object()
    #    return Response(demand.highlighted)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        created_date=timezone.now())



class PositionViewSet(viewsets.ModelViewSet):
    # position =Position.objects.all()
    # demands = get_object_or_404(Demand, id=demand)
    queryset = Position.objects.all()
    serializer_class =  PositionSerializer
    filter_fields = ('demand',)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #                       IsOwnerOrReadOnly,)

# class DemandIDPosViewSet(viewsets.ModelViewSet):
#     queryset = Demand.objects.all()
#     serializer_class = DemandIDPosSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user,
#                         created_date=timezone.now())



                    

