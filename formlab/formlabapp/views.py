from django.shortcuts import render,redirect
from.models import *
from.forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request,"home.html")

def mpsc(request):
    return render (request,"test.html")

def signup(request):
    telu = userinfo.objects.all()
    return render(request,"signup/index.html",{"telu":telu})

def webhome(request):
    return render (request,"index.html")

def display(request):
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            birthday = request.POST["birthday"]
            city = request.POST["city"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            regi = registration(first_name=first_name,last_name=last_name,birthday=birthday,city=city,email=email,phone=phone)
            regi.save()
            return render(request,"display.html")


def register(request):
    if request.method == 'POST':
        forms = registration_form(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/register/')

    else:
        forms = registration_form()
    return render(request,'signup.html',{"forms":forms})


def login(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username1 = form1.cleaned_data['username']
            email1 = form1.cleaned_data['email']
            first_name1 = form1.cleaned_data['first_name']
            last_name1 = form1.cleaned_data['last_name']
            password1 = form1.cleaned_data['password']
            User.objects.create_user(username=username1,first_name=first_name1,last_name=last_name1,email=email1,password=password1)
            messages.success(request,'User registration Succsessfully')
            return HttpResponseRedirect('/login/')
    else:
        form1 = userform()
    return render(request,'signup.html',{'frm':form1})

def enter(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,"file.html")
            else:
                messages.error(request,"username or password did not match")
        except auth.ObjectNotExist:
            print("Invalid User")
    return render(request,'enter.html')


def logout(request):
    auth.logout(request)
    return render(request,"enter.html")
def file(request):
    return render (request,"file.html")





