from django.shortcuts import render

from .forms import PictureForm
from .models import Picture

def index(request):
    return render(request,"app_photo/index.html", context={'msg':'Hello World!'})

def pictures(request):
    return render(request,"app_photo/pictures.html", context={'msg':'Hello World!'})

def upload(request):
    form = PictureForm(instance=Picture())
    return render(request,"app_photo/upload.html", context={'form':'form'})

