from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from .models import Form


# Create your views here.

def index1(request):
    return render(request, 'index1.html')


def display_data(request):
    forms = Form.objects.all()
    return render(request, 'redirect_profile.html', {'forms': forms})


def getdata1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        picture = request.FILES['picture']
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        bio = request.POST.get('bio')
        j_role = request.POST.get('job')
        interests = request.POST.get('interest')
        form = Form(name=name, picture=picture, email=email, password=password, birthday=birthday, bio=bio,
                    j_role=j_role,
                    interests=interests)
        form.save()
        return redirect('display_data')
    else:
        return HttpResponse('Complete the form !!')


def delete_form(request, id):
    Form.objects.get(id=id).delete()
    return redirect('display_data')


def update_form(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        bio = request.POST.get('bio')
        j_role = request.POST.get('job')
        interests = request.POST.get('interest')

        try:
            img_p = request.FILES['picture']
            fs = FileSystemStorage()
            file = fs.save(img_p.name, img_p)
        except MultiValueDictKeyError:
            file = Form.objects.get(id=id).image

        Form.objects.filter(id=id).update(name=name, picture=file, email=email, password=password, birthday=birthday,
                                          bio=bio, j_role=j_role,
                                          interests=interests)
        return redirect('display_data')
