from django.core.files.storage import FileSystemStorage
from django.shortcuts import HttpResponse, render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Contact


# Create your views here.
def index(request):
    return render(request, "index.html")


def profile(request):
    contacts = Contact.objects.all()
    return render(request, 'redirect_page.html', {'contacts': contacts})


def getdata(request):
    if request.method == "POST":
        usn = request.POST.get('usn')
        name = request.POST.get('name')
        pic = request.POST.get('pic')
        sem = request.POST.get('sem')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact = Contact(usn=usn, name=name, sem=sem, phone=phone, email=email, pic=pic)
        contact.save()
        return redirect('profile')
    else:
        return HttpResponse('Complete the form and try again!!')


def delete_contact(request, usn):
    Contact.objects.get(usn=usn).delete()
    return redirect('profile')


def update_contact(request,usn):
        if request.method == 'POST':
            usn = request.POST.get('usn')
            name = request.POST.get('name')
            pic = request.POST.get('pic')
            sem = request.POST.get('sem')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            Contact.objects.filter(usn=usn).update(usn=usn, name=name, sem=sem, phone=phone, email=email, pic=pic)
        return redirect('profile')

