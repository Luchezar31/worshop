from django.urls import path

from common import views

urlpatterns = [
    path('',views.common_view,name='home-page')
]