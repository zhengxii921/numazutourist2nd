from django.test import TestCase
from numazutourist.models import *

# Create your tests here.

class PlaceModelTests(TestCase):


    # 空の状態にカウントして0かどうか
    def test_is_empty(self):
        saved_places = Place.objects.all()
        self.assertEqual(saved_places.count(),0)


    # 1つ足して要素が1つ増えるかどうか
    def test_is_count_one(self):
        place = Place(
            name="name",
            adress="Tokyo",
            explain="here",
            sort=1,
            opentime="00:00:00",
            closetime="23:59:59",
        )
        place.save()
        saved_places = Place.objects.all()
        self.assertEqual(saved_places.count(),1)


    # 保存して取り出して元の名前と一致するかどうか
    def test_savind_and_retrieving_place(self):
        place = Place()
        name = "name"
        place.name=name
        place.adress="Tokyo"
        place.explain="here"
        place.sort=1
        place.opentime="00:00:00"
        place.closetime="23:59:59"
        place.save()
        saved_places = Place.objects.all()
        actual_place = saved_places[0]

        self.assertEqual(actual_place.name, name)


    def test_over_length(self):
        time = "24:59:59"
        place = Place(
            name="name",
            adress="Tokyo",
            explain="here",
            sort=1,
            opentime="00:00:00",
            closetime=time,
        )

        self.assertEqual(place.closetime, time)


class LovenumaModelTests(TestCase):


    def test_is_empty(self):
        saved_lovenuma = Lovenuma.objects.all()