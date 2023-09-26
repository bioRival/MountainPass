from django.test import TestCase
from core.models import Users, Coords


class EmailUnique(TestCase):
    def set_up(self):
        user_setup = Users.objects.create(
            email="tester@gmail.com",
            phone = "+12345678900",
            surname = "Smith",
            firstname = "Bob",
            patronymic = "Bobovich"
        )

        return user_setup

    def try_create_same_email(self):
        user_setup = Users.objects.create(
            email="tester@gmail.com",
            phone = "+12345678900",
            surname = "Gavin",
            firstname = "John",
            patronymic = "Malkovich"
        )

        return user_setup

    def test_this_thing(self):
        user = self.set_up()
        user2 = self.try_create_same_email()

class CoordsCorrect(TestCase):
    def wrong_type_latitude_longitude():
        list_of_values = [100, 100.500, "100", True, "pizza"]
        for value in list_of_values:
            Coords.objects.create(
                latitude = value,
                longitude = value,
                height = 100
            )