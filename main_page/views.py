from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    # print(request.method)
    return render(request, 'main_page/main.html', context)


def about(request):
    return render(request, 'main_page/about.html', {'title': 'About page'})

# Create your views here.
