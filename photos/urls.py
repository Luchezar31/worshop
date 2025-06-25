from django.urls import path, include

from photos import views

urlpatterns = [
    path('', include([
        path('add/', views.photos_add_view, name='photos-add'),
        path('<int:pk>/', views.photos_details_views, name='photos-details'),
        path('<int:pk>/edit/', views.photos_edit_view, name='photos-edit')
    ]))
]
