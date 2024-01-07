import factory
from places.models import Place

class PlaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Place
    name = factory.Sequence(lambda n: f"Name of place number {n}")
    location = factory.Sequence(lambda n: f"Location of place number {n}")
    description = factory.Sequence(lambda n: f"Description of place number {n}")

