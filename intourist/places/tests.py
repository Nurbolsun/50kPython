from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place
from .factories import PlaceFactory
# Create your tests here.

# class PlacesListTestCase(TestCase):
#     def test_open_list_succes(self):
#         url = reverse('places-list')
#         response = self.client.get('/places/')
#         print(response.status_code)
#         self.assertEqual(response.content, 'places')
#         self.assertIsInstance(response.content.get('places'), QuerySet)

class PlacesListTestCase(TestCase):
    def test_open_list_succes(self):
        place_1 = PlaceFactory()
        place_2 = PlaceFactory()

        url = reverse('places-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        places = response.context.get('places')
        self.assertIsInstance(places, QuerySet)
        print(places)

        self.assertEqual('Location - 1', places[1].location)

class PlaceCreateTestCase(TestCase):
    def test_place_create_succes(self):
        url = reverse('create-place')
        data = {
            'name': 'Aigul gulu',
            'location': 'Batken rejion',
            'description': 'Mountains and flowers in KG'
        }
        response = self.client.post(url, data)
        place = Place.objects.last()
        self.assertEqual(place.name, 'Aigul gulu')
    
