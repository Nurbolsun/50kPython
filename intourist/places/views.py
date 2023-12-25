from django.shortcuts import render, HttpResponse
from .models import Place
# Create your views here.

def places(request):
    place_obj = Place.objects.all() #selec from *
    return render(request, 'places.html', {'places' : place_obj})