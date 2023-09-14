from .models import Users, Coords, Images, PerevalAdded, ActivityTypes, Areas
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Users
       fields = ['id', 'email', 'phone', 'surname', 'firstname', 'patronymic', ]


class CoordsSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Coords
       fields = ['id', 'latitude', 'longitude', 'height', ]


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Images
       fields = ['id', 'name', 'photos', ]


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = PerevalAdded
       fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'spring', 'summer', 'autumn', 'winter',
                 'photos', 'add_time', 'coords', 'author', 'status']


class ActivityTypesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = ActivityTypes
       fields = ['id', 'title', ]


class AreasSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Areas
       fields = ['id', 'id_parent', 'title', ]