from django.shortcuts import render

from pets.models import Pet


def add_pet_view(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details_view(request, username, pet_slug):
    pet = Pet.objects.prefetch_related('photos').get(slug=pet_slug)
    photos = pet.photos.prefetch_related('tagged_pets').all()

    context = {
        'pet':pet,
        'photos':photos
    }

    return render(request, 'pets/pet-details-page.html',context)


def pet_edit_view(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete_view(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
