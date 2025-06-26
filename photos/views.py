from django.shortcuts import render

from photos.models import Photo


# Create your views here.
def photos_add_view(request):
    return render(request, 'photos/photo-add-page.html')


def photos_details_views(request, pk):
    photo = Photo.objects.prefetch_related('comment_set').get(pk=pk)
    comments = photo.comment_set.all()

    context = {
        'photo':photo,
        'comments':comments
    }

    return render(request, 'photos/photo-details-page.html',context)


def photos_edit_view(request, pk):
    return render(request, 'photos/photo-edit-page.html')