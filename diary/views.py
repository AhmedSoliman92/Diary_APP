from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def add(request):
    context = {}
    return render(request, 'add-diary.html', context)
