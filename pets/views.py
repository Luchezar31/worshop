from django.shortcuts import render, redirect

from pets.forms import PetCreateForm, PetEditForm
from pets.models import Pet


def add_pet_view(request):
    create_form = PetCreateForm(request.POST or None)

    if request.method == 'POST' and create_form.is_valid():
        create_form.save()

        return redirect('profile-page', pk=1)

    context = {
        'create_form': create_form
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details_view(request, username, pet_slug):
    pet = Pet.objects.prefetch_related('photos').get(slug=pet_slug)
    photos = pet.photos.prefetch_related('tagged_pets').all()

    context = {
        'pet': pet,
        'photos': photos
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit_view(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    edit_form = PetEditForm(request.POST or None,instance=pet)

    if request.method == 'POST' and edit_form.is_valid():
        edit_form.save()
        return redirect('details-pets', username='Username',pet_slug=pet.slug)

    context = {
        'edit_form': edit_form,
        'pet':pet
    }
    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete_view(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
