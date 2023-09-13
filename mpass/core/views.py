from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from core.serializers import *
from core.models import Users, DifficultyLevels, Coords, Images, PerevalAdded, ActivityTypes, Areas


class UsersViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = UsersSerializer


class DifficultyLevelsViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = DifficultyLevelsSerializer


class CoordsViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = CoordsSerializer


class ImagesViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = ImagesSerializer


class PerevalAddedViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = PerevalAddedSerializer


class ActivityTypesViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = ActivityTypesSerializer


class AreasViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = AreasSerializer

