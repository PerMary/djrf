from .models import Demand, Position
from demands.serializers import DemandSerializer, PositionSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from demands.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action




class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

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
    queryset = Position.objects.all()
    serializer_class =  PositionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)



# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'demands': reverse('demand-list', request=request, format=format)
#     })
#

                    

