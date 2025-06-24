from django.shortcuts import render

from photos.models import Photo


# Create your views here.
def common_view(request):

    all_photos = Photo.objects.all()

    context = {
        'all_photos':all_photos
    }

    return render(request,'common/home-page.html',context)

