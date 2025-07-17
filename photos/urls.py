from django.urls import path, include

from photos import views

urlpatterns = [
    path('', include([
        path('add/', views.CreatePhoto.as_view(), name='photos-add'),
        path('<int:pk>/', views.PhotoDetails.as_view(), name='photos-details'),
        path('<int:pk>/edit/', views.PhotoEdit.as_view(), name='photos-edit'),
        path('<int:pk>/delite/',views.photos_delete_view,name='photo-delete')
    ]))
]
