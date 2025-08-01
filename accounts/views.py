from django.shortcuts import render


# Create your views here.
def account_view(request):
    return render(request, 'accounts/register-page.html')


def login_view(request):
    return render(request, 'accounts/login-page.html')


def profile_details_view(request, pk):
    content = {
        'pk_id': 1
    }
    return render(request, 'accounts/profile-details-page.html', content)


def profile_edit_view(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def profile_delete_view(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
