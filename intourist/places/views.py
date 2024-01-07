from django.shortcuts import render, HttpResponse, redirect
from .models import Place
from .forms import PlaceForm, FeedbackForm
from django.views.generic import FormView
# Create your views here.

def places(request):
    place_obj = Place.objects.all() #selec from *
    return render(request, 'places/places.html', {'places' : place_obj})

def create_place(request):
    if request.method == "POST":
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect(places)
    place_form = PlaceForm()
    return render(request, 'places/form.html', {'place_form': place_form}) 

def place(request, id):
    place_obj = Place.objects.get(id=id)
    place_obj.views_count = place_obj.views_count + 1
    place_obj.save()
    return render(request, 'places/place.html', {'place_obj': place_obj})

def edit_place(request, id):
    place_obj = Place.objects.get(id=id)
    if request.method == "POST":
        place_form = PlaceForm(data=request.POST, instance=place_obj)
        place_form.save()
        return redirect(place, id=id)

    place_form = PlaceForm(instance=place_obj)
    return render(request, 'places/form.html', {'place_form': place_form})

def delete_place(request, id):
    place_obj = Place.objects.get(id=id)
    place_obj.delete()
    return redirect(places)

class Cbv:
    def my_method(self):
        return HttpResponse('This Page Working Yaa')
    
class FeedbackView(FormView):
    template_name = 'places/feedback_form.html'
    form_class = FeedbackForm
    success_url = '/places/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
