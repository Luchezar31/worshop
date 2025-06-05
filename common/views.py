from django.shortcuts import render

# Create your views here.
def common_view(request):
    return render(request,'common/home-page.html')

