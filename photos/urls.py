from django.urls import path, include

from photos import views

urlpatterns = [
    path('photos/', include([
        path('add/', views.photos_add_view, name='photos-add'),
        path('<int:pk>/', views.photos_details_views, name='photos_details'),
        path('<int:pk>/edit/', views.photos_edit_view, name='photos_edit')
    ]))
]
