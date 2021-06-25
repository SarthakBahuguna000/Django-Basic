from urllib import request

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("successful")


    else:
        return render(request,'login.html')
def register(register):
    if request.method=='POST':
        FirstName=request.POST['FirstName']
        email = request.POST['email']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        address=request.POST['address']
        if password1==password2:
            if User.objects.filter(username=FirstName).exits():
                print("Username Taken")
            else:
                user=User.objects.create_user(email=email,password=password1,Name=FirstName,address=address)
                user.save();
                print("Successfully Created")
        else:
            print('password not matched')
    else:
         return render(request,'register.html')