from django.urls import path, include
from pets import views


urlpatterns = [
    path('',views.add_pet_view,name='add-pets'),
    path('<str:username>/pet/<slug:pet_slug>/',include([
        path('',views.pet_details_view,name='details-pets'),
        path('edit/',views.pet_edit_view,name='edit-pets'),
        path('delete/',views.pet_delete_view,name='delete-pets')
    ]))
]