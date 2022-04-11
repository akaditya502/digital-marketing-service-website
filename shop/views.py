from django.shortcuts import render
from datetime import datetime
from shop.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
#def contact(request):
    #return render(request,'contact.html')
def services(request):
    return render(request,'services.html')


def seo(request):
    return render(request,'seo.html')
def ppc(request):
    return render(request,'ppc.html')
def marketing(request):
    return render(request,'marketing.html')
def webdesign(request):
    return render(request,'webdesign.html')
def webdevelopement(request):
    return render(request,'webdevelopement.html')






def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
       


        
        email = request.POST.get('email')
        

       # password = request.POST.get('password')
        comment = request.POST.get('comment')

        
        contact = Contact(firstname=firstname,lastname=lastname, email=email, comment=comment,date=datetime.today())
        messages.success(request, 'your messages has been sent.')
        contact.save()

    return render(request,'contact.html')  

    

