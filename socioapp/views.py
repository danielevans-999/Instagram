from django.shortcuts import render,redirect
from . forms import ImageUploadForm
from .models import *

def home(request):
    images = Image.objects.all()
    return render(request, 'socioapp/index.html',{"images":images})

def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ImageUploadForm()
        return render(request,'socioapp/upload.html', {"form":form})
