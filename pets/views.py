from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from common.forms import AddCommentForm
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet



class CreatePet(CreateView):
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-page',kwargs={'pk':1})

    # need to be overwritten if the form is not passed as form
    # def get_context_data(self,**kwargs):
    #     kwargs.update({
    #         'create_form': self.get_form_class()
    #     })
    #     return super().get_context_data(**kwargs)

# def add_pet_view(request):
#     create_form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST' and create_form.is_valid():
#         create_form.save()
#
#         return redirect('profile-page', pk=1)
#
#     context = {
#         'create_form': create_form
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)




class PetDetails(DetailView):
    model = Pet
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self,*args,**kwargs):
        kwargs.update({
            'photos': self.object.photos.prefetch_related('tagged_pets').all(),
            'add_comment_form': AddCommentForm()
        })

# def pet_details_view(request, username, pet_slug):
#     pet = Pet.objects.prefetch_related('photos').get(slug=pet_slug)
#     photos = pet.photos.prefetch_related('tagged_pets').all()
#     add_comment_form = AddCommentForm(request.POST or None)
#
#     context = {
#         'pet': pet,
#         'photos': photos,
#         'add_comment_form':add_comment_form
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class PetEdit(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('details-pets', kwargs={
            'username':self.kwargs.get('username'),
            'pet_slug':self.kwargs.get('pet_slug')
        })


# def pet_edit_view(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     edit_form = PetEditForm(request.POST or None,instance=pet)
#
#     if request.method == 'POST' and edit_form.is_valid():
#         edit_form.save()
#         return redirect('details-pets', username='Username',pet_slug=pet.slug)
#
#     context = {
#         'edit_form': edit_form,
#         'pet':pet
#     }
#     return render(request, 'pets/pet-edit-page.html', context)


class DeletePet(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('profile-page',kwargs={'pk':1})
    template_name = 'pets/pet-delete-page.html'

    def get_initial(self):
        return self.object.__dict__

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({
    #         'data': self.get_initial()
    #     })
    #     return kwargs




