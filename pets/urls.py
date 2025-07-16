from django.urls import path, include
from pets import views


urlpatterns = [
    path('',views.CreatePet.as_view(),name='add-pets'),
    path('<str:username>/pet/<slug:pet_slug>/',include([
        path('',views.PetDetails.as_view(),name='details-pets'),
        path('edit/',views.PetEdit.as_view(),name='edit-pets'),
        path('delete/',views.DeletePet.as_view(),name='delete-pets')
    ]))
]