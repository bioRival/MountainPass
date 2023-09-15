"""
URL configuration for mpass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from core.views import (UsersViewset, CoordsViewset, ImagesViewset, PerevalAddedViewset,
                        ActivityTypesViewset, AreasViewset)

router = routers.DefaultRouter()
router.register(r'users', UsersViewset)
router.register(r'coordinates', CoordsViewset)
router.register(r'photos', ImagesViewset)
router.register(r'submitData', PerevalAddedViewset)
router.register(r'activity_types', ActivityTypesViewset)
router.register(r'areas', AreasViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
