from django.shortcuts import render,redirect
import hashlib
from .models import Credential
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate
# Create your views here.



def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        compassword = req.POST['c_password']
        account_type = req.POST['account_type']

       
        if password == compassword:
            if User.objects.filter(username=username).exists():
                messages.info(req, "Username Already Taken")
                return redirect('reg:register')
            elif User.objects.filter(email=email).exists():
                messages.info(req, "Email Already Taken")
                return redirect('reg:register')
            
            else:
              user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_staff=account_type)
              return redirect('reg:login')


        else:
            messages.info(req, "Passwords do not match")
            return redirect('reg:register')

    

    return render(req,'register.html')

def login(req):
   if req.method=='POST':
      username=req.POST['username']
      password=req.POST['password']
      user=auth.authenticate(username=username,
        password=password)
      
     
      if user is not None:
            auth.login(req,user)
            return redirect('/')
      else:
            messages.info(req,"invalid User")
            return redirect('reg:login')
   return render(req,'login.html')




