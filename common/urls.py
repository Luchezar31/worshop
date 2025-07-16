from django.urls import path

from common import views

urlpatterns = [
    path('',views.CommonView.as_view(),name='home-page'),
    path('like/<int:photo_id>/',views.like,name='like'),
    path('share/<int:photo_id>/',views.share,name='share'),
    path('comment/<int:photo_id>/',views.add_comment_view,name='add-comment')
]


