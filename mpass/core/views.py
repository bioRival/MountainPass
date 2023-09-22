from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response

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

   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

   def partial_update(self, request, pk=None, *args, **kwargs):
      mpass = self.get_object()
      if mpass.status == '1':
         serializer = PerevalAddedSerializer(mpass, data=request.data, partial=True)
         if serializer.is_valid():
            serializer.save()
            return Response(
               {
                  'state': '1',
                  'message': 'Information was successfully edited'
               }
            )
         else:
            return Response(
               {
                  'state': '0',
                  'message': serializer.errors
               }
            )
      else:
         return Response(
            {
               'state': '0',
               'message': f'Error. Status of this instance is: *{mpass.get_status_display()}*.' \
                          f' You can only edit the ones with the status of *new*'
            }
         )


class ActivityTypesViewset(viewsets.ModelViewSet):
   queryset = ActivityTypes.objects.all()
   serializer_class = ActivityTypesSerializer


class AreasViewset(viewsets.ModelViewSet):
   queryset = Areas.objects.all()
   serializer_class = AreasSerializer

