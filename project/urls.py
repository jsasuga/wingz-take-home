"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import UserViewSet, RideViewSet, RideEventViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

router = DefaultRouter()

router.register(r'user', UserViewSet, 'user')
router.register(r'ride', RideViewSet, 'ride')
router.register(r'ride_event', RideEventViewSet, 'ride_event')

schema_view = get_schema_view(
    openapi.Info(
        title="wingz",
        default_version='v1',
        description="API description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger(<format>)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                            cache_timeout=0), name='schema-swagger-ui'),
]
