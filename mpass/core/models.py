from django.db import models
from django.utils import timezone

# Grades of difficulty to pass a terrain
DIFFICULTY = [
    ('00', 'Неизвестно'),
    ('1A', '1А'),
    ('1B', '1Б'),
    ('2А', '2А'),
    ('2В', '2Б'),
    ('3А', '3А'),
    ('3В', '3Б'),
    ]

# Status of added info, new by default
STATUS = [
    ('1', 'new'),
    ('2', 'pending'),
    ('3', 'accepted'),
    ('4', 'rejected'),
]

class Users(models.Model):
    """
    Information about a person submitting data, email must be unique
    """

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.surname} {self.email}"


class Coords(models.Model):
    """
    Coordinates of the subject's location taking photos of mountain pass
    """
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    height = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.latitude} {self.longitude} {self.height}"


class Images(models.Model):
    """
    Photo info, currently in char form
    """
    name = models.CharField(max_length=255, blank=True)
    photo = models.TextField(blank=True)


class PerevalAdded(models.Model):
    """
    Subbmited data about one of the passes
    """
    beauty_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)

    connect = models.CharField(max_length=255, blank=True)
    photos = models.ManyToManyField(Images, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    # Difficulty level of movement during each season
    spring = models.CharField(max_length=2, choices=DIFFICULTY, default='00')
    summer = models.CharField(max_length=2, choices=DIFFICULTY, default='00')
    autumn = models.CharField(max_length=2, choices=DIFFICULTY, default='00')
    winter = models.CharField(max_length=2, choices=DIFFICULTY, default='00')

    status = models.CharField(choices=STATUS, max_length=1, default='1')

    def __str__(self):
        return self.title


class ActivityTypes(models.Model):
    """
    Activity Types recreated from old database, currently unused
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Areas(models.Model):
    """
    Areas recreated from old database, currently unused
    """
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE, default=1, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
