from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from demands import views
from demands.views import DemandViewSet, UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from demands import views
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'demands', views.DemandViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'positions', views.PositionViewSet)

#schema_view = get_schema_view(title='Example API')

urlpatterns = [
    #path('schema/', schema_view),
    path('', include(router.urls)),
]


# demand_list = DemandViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# demand_detail = DemandViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# demand_highlight = DemandViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('demands/',
#          demand_list,
#          name='demand-list'),
#     path('demands/<int:id_demand>/',
#          demand_detail,
#          name='demand-detail'),
#     path('users/',
#          user_list,
#          name='user-list'),
#     path('users/<int:id_demand>/',
#          user_detail,
#          name='user-detail'),
#     path('demands/<int:id_demand>/highlight/',
#          demand_highlight,
#          name='demand-highlight'),
# ])



