from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.models import Like
from photos.models import Photo


# Create your views here.
def common_view(request):
    all_photos = Photo.objects.prefetch_related('comment_set').all()

    context = {
        'all_photos':all_photos
    }
    return render(request,'common/home-page.html',context)

def like(request,photo_id):

    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(to_photo_id=photo_id)

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

def share(request,photo_id):

    copy(request.META['HTTP_HOST'] + resolve_url('photos-details',photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')