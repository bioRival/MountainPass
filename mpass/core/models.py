from django.db import models
from django.utils import timezone


DIFFICULTY = [
    ('00', 'Неизвестно'),
    ('1A', '1А'),
    ('1B', '1Б'),
    ('2А', '2А'),
    ('2В', '2Б'),
    ('3А', '3А'),
    ('3В', '3Б'),
    ]

STATUS = [
    ('1', 'new'),
    ('2', 'pending'),
    ('3', 'accepted'),
    ('4', 'rejected'),
]

class Users(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.surname} {self.email}"


class DifficultyLevels(models.Model):
    spring = models.CharField(max_length=2, choices=DIFFICULTY)
    summer = models.CharField(max_length=2, choices=DIFFICULTY)
    autumn = models.CharField(max_length=2, choices=DIFFICULTY)
    winter = models.CharField(max_length=2, choices=DIFFICULTY)

    def __str__(self):
        return f'SPRING: {self.spring},\n' \
               f'SUMMER: {self.summer},\n' \
               f'AUTUMN: {self.autumn},\n' \
               f'WINTER: {self.winter}'


class Coords(models.Model):
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    height = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.latitude} {self.longitude} {self.height}"


class Images(models.Model):
    name = models.CharField(max_length=255, blank=True)
    photos = models.TextField(blank=True)


class PerevalAdded(models.Model):
    beautyTitle = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.CharField(max_length=255, blank=True)
    difficulty = models.ForeignKey(DifficultyLevels, on_delete=models.CASCADE, blank=True)
    photos = models.ForeignKey(Images, on_delete=models.CASCADE, blank=True)
    add_time = models.DateTimeField(default=timezone.now, editable=False)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=1, default='1')

    def __str__(self):
        return self.title


class ActivityTypes(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Areas(models.Model):
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE, default=1, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
