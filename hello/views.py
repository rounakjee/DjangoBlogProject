from django.shortcuts import render
from .models import Posts


def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, "hello/home.html", context)


def about(request):
    return render(request, "hello/about.html")

