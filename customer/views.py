from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth


# Create your views here.
def chef(request):
    return render(request,'chef.html')
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def order(request):
    return render(request,'order.html')
def foods(request):
    return render(request,'foods.html')
def foodsearch(request):
    return render(request,'foodsearch.html')
def contact(request):
    return render(request,'contact.html')
def categories(request):
    return render(request,'categories.html')
def categoryfoods(request):
    return render(request,'categoryfoods.html')
def register(request):
    if request.method=="POST":
        um=request.POST['username']
        em=request.POST['email']
        psw=request.POST['password']
        cpsw=request.POST['cpassword']
        if psw==cpsw:
            if User.objects.filter(username=um).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email exist")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(username=um,email=em,password=cpsw)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"passwrd nt matching")
            return render(request,"register.html")
    
    return render(request,'register.html')
def login(request):
    if request.method=="POST":
        un=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=un,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
        
    return render(request,'login.html')
