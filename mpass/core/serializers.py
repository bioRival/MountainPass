from .models import Users, Coords, Images, PerevalAdded, ActivityTypes, Areas, DIFFICULTY, STATUS
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    # Canceling Unique check for email, because it breaks get_or_create() in PerevalAddedSerializer
    email = serializers.EmailField(validators=[])
    class Meta:
        model = Users
        fields = ['id', 'email', 'phone', 'surname', 'firstname', 'patronymic', ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['id', 'latitude', 'longitude', 'height', ]


class ImagesSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'name', 'photo', ]


class PerevalAddedSerializer(WritableNestedModelSerializer):
    author = UsersSerializer()
    photos = ImagesSerializer(many=True)
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'spring', 'summer', 'autumn', 'winter',
                  'coords', 'status', 'author', 'photos']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        photos_data = validated_data.pop('photos')
        coords_data = validated_data.pop('coords')

        # Searches user by Email, if they exist - fetches the instance, if don't - creates a new one.
        # "created" bool variable won't be used later, it's just a requirement for ger_or_create()
        author, created = Users.objects.get_or_create(email=author_data['email'], defaults={**author_data})

        coords = Coords.objects.create(**coords_data)

        mpass = PerevalAdded.objects.create(**validated_data, author=author, coords=coords)

        # Photos, if any, are tied to this instance by ManyToMany link
        if photos_data:
            for photo in photos_data:
                name = photo.pop('name')
                photo_data = photo.pop('photo')
                image = Images.objects.create(name=name, photo=photo_data)
                mpass.photos.add(image)

        mpass.save()
        return mpass

    def validate(self, data):
        if self.instance is not None:
            author = self.instance.author
            author_data = data.get('author')
            fields_check = [
                author.surname != author_data['surname'],
                author.firstname != author_data['firstname'],
                author.patronymic != author_data['patronymic'],
                author.phone != author_data['phone'],
                author.email != author_data['email'],
            ]
            if author_data is not None and any(fields_check):
                raise serializers.ValidationError(
                    {
                        'error': 'Cant edit user information',
                    }
                )
        return data


class ActivityTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTypes
        fields = ['id', 'title', ]


class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ['id', 'id_parent', 'title', ]
