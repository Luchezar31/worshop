from django.shortcuts import render


# Create your views here.
def photos_add_view(request):
    return render(request, 'photos/photo-add-page.html')


def photos_details_views(request, pk):
    return render(request, 'photos/photo-details-page.html')


def photos_edit_view(request, pk):
    return render(request, 'photos/photo-edit-page.html')