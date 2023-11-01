from django.shortcuts import render
from . models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')


def generic(request):
    return render(request, 'generic.html')

def elements(request):
    return render(request, 'elements.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        contact=Contact(name=name ,email=email,message=message)
        contact.save()
        
    return render(request,"sucess.html")