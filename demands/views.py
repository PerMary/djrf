from .models import Demand, Position
from demands.serializers import DemandSerializer, PositionSerializer
from django.conf import settings
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from weasyprint import HTML, CSS
import datetime
from django.template.loader import render_to_string
from documents.models import Document
from django.contrib.auth import get_user_model

User=get_user_model()




class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer


    # def list(self, request, *args, **kwargs):
    #     queryset = Demand.objects.all()
    #     seriaizer = DemandSerializer(queryset, many=True)
    #     return Response (seriaizer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Demand.objects.all()
    #     demand = get_object_or_404(queryset, pk=pk)
    #     seriaizer = DemandPosSerializer(demand)
    #     return Response(seriaizer.data)
    # # эта штука в список выводит все заявки заявки без позиций, но если перейти к
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

    @action(detail=True)
    def PDF(self, request, *args, **kwargs):
        demand = self.get_object()
        positions = Position.objects.filter(demand=demand)
        today_date = datetime.datetime.today()
        template_string = render_to_string('documents/PDF_for_demand.html', {'demand': demand,
                                                                             'positions': positions,
                                                                             'today_date': today_date,
                                                                             'user': request.user})
        html = HTML(string=template_string)
        file_name = 'Demand_' + str(demand.id) + '_' + str(today_date.strftime('%Y-%m-%d_%H.%M.%S')) + '_detail' + '.pdf'
        path_name = settings.MEDIA_ROOT + '/' + file_name
        html.write_pdf(path_name)
        url_name = settings.MEDIA_URL + file_name
        Document.objects.create(date_create=today_date,
                                user_create= request.user,
                                demand = demand,
                                name_doc= file_name,
                                url = url_name,
                                )
        demand.changed = False
        demand.save()
        return Response(url_name)




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



                    

