from django.urls import path
from .views import places, create_place, place, edit_place, delete_place, Cbv, FeedbackView

urlpatterns = [
    path('', places, name = 'places-list'),
    path('create/', create_place, name='create-place'),
    path('<int:id>/', place, name='place'),
    path('<int:id>/edit', edit_place, name='edit-place'),
    path('<int:id>/delete', delete_place, name='delete-place'),
    path('cbv/', Cbv.my_method, name='cbv'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),

    
]