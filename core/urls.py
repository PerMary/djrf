"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from demands.views import DemandViewSet, PositionViewSet
from  users.views import UserViewSet, ProfileViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   # TODO: write something reasonable below
   openapi.Info(

      title="EXAMPLE API",
      default_version='v0',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'demands', DemandViewSet)
router.register(r'users', UserViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('schema/', schema_view),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
