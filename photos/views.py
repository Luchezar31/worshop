from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from common.forms import AddCommentForm
from photos.forms import PhotoAddForm, PhotoEditForm
from photos.models import Photo




class CreatePhoto(CreateView):
    model = Photo
    form_class = PhotoAddForm
    success_url = reverse_lazy('home-page')
    template_name = 'photos/photo-add-page.html'

    def get_context_data(self,**kwargs):
        kwargs.update({
            'add_form': self.get_form_class()
        })
        return super().get_context_data(**kwargs)

# def photos_add_view(request):
#     add_form = PhotoAddForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST' and add_form.is_valid():
#         add_form.save()
#         return redirect('home-page')
#
#     context = {
#         'add_form':add_form
#     }
#     return render(request, 'photos/photo-add-page.html', context)


class PhotoDetails(DetailView):
      model = Photo
      template_name = 'photos/photo-details-page.html'

      def get_context_data(self,**kwargs):
          kwargs.update({
              'add_comment_form': AddCommentForm(),
              'comments': self.object.comment_set.all()
          })
          return super().get_context_data(**kwargs)

# def photos_details_views(request, pk):
#     photo = Photo.objects.prefetch_related('comment_set').get(pk=pk)
#     comments = photo.comment_set.all()
#     add_comment_form = AddCommentForm(request.POST or None)
#     context = {
#         'photo':photo,
#         'comments':comments,
#         'add_comment_form':add_comment_form
#     }
#
#     return render(request, 'photos/photo-details-page.html',context)


class PhotoEdit(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    success_url = reverse_lazy('home-page')
    template_name = 'photos/photo-edit-page.html'

    def get_context_data(self,**kwargs):
        kwargs.update({
            'edit_form':self.get_form()
        })
        return super().get_context_data(**kwargs)

    def get_initial(self):
        return self.object.__dict__

# def photos_edit_view(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     edit_form = PhotoEditForm(request.POST or None,instance=photo)
#
#     if request.method == 'POST' and edit_form.is_valid():
#         edit_form.save()
#         return redirect('home-page')
#
#     context = {
#         'photo':photo,
#         'edit_form':edit_form
#     }
#
#     return render(request, 'photos/photo-edit-page.html',context)

def photos_delete_view(request,pk):
    photo = Photo.objects.get(pk=pk)

    photo.delete()

    return redirect('home-page')