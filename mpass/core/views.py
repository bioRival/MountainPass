from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

from core.serializers import *
from core.models import Users, Coords, Images, PerevalAdded, ActivityTypes, Areas


class UsersViewset(viewsets.ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer


class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordsSerializer


class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer


class PerevalAddedViewset(viewsets.ModelViewSet):
   queryset = PerevalAdded.objects.all()
   serializer_class = PerevalAddedSerializer


class ActivityTypesViewset(viewsets.ModelViewSet):
   queryset = ActivityTypes.objects.all()
   serializer_class = ActivityTypesSerializer


class AreasViewset(viewsets.ModelViewSet):
   queryset = Areas.objects.all()
   serializer_class = AreasSerializer

