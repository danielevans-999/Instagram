from django.shortcuts import render,redirect
from . forms import ImageUploadForm,ImageProfileForm
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
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
    
def profile_info(request):
    profile_info = Profile.objects.first()
    posts =  request.user.image_set.all()
    
    
    return render(request,'socioapp/profile.html',{"images":posts,"profile":profile_info})
        
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ImageProfileForm()
        return render(request,'socioapp/edit.html',{"form":form})
    
    
    
    
