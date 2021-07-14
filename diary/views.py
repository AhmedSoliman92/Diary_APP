from diary.models import DiaryModel
from django.shortcuts import redirect, render
from .form import DiaryForm
# Create your views here.


def index(request):
    diaries = DiaryModel.objects.order_by('-time')
    context = {'diaries': diaries}
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = DiaryForm()
    context = {'form': form}
    return render(request, 'add.html', context)
