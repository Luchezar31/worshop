from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from pyperclip import copy

from common.forms import AddCommentForm, SearchForm
from common.models import Like
from photos.models import Photo


class CommonView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self,object_list=None,**kwargs):
        kwargs.update({
            'add_comment_form': AddCommentForm(),
            'search_form': SearchForm()
        })
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('text')

        if pet_name is not None:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)

        return queryset





# def common_view(request):
#     all_photos = Photo.objects.prefetch_related('comment_set').all()
#     add_comment_form = AddCommentForm(request.POST or None)
#     search_form = SearchForm(request.GET or None)
#
#     if search_form.is_valid():
#         all_photos=Photo.objects.filter(
#             tagged_pets__name__icontains=search_form.cleaned_data['text']
#         )
#
#
#     context = {
#         'all_photos':all_photos,
#         'add_comment_form':add_comment_form,
#         'search_form':search_form
#     }
#     return render(request,'common/home-page.html',context)

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


def add_comment_view(request,photo_id):
    form = AddCommentForm(request.POST or None)
    photo = Photo.objects.get(pk=photo_id)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

