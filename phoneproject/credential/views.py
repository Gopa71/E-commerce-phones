from django.shortcuts import render,redirect
import hashlib
from .models import Credential 
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login
# Create your views here.


def md5_hash(password):
    """Hashes the password using MD5."""
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        compassword = req.POST['c_password']
       
        if password == compassword:
            if Credential.objects.filter(username=username).exists():
                messages.info(req, "Username Already Taken")
                return redirect('register')
            elif Credential.objects.filter(email=email).exists():
                messages.info(req, "Email Already Taken")
                return redirect('reg:register')
            else:
                hashed_password = md5_hash(password)
                print("asd",hashed_password)
                user = Credential(username=username, first_name=first_name, last_name=last_name, email=email, password=hashed_password)
                user.save()
                return redirect('reg:login')
        else:
            messages.info(req, "Passwords do not match")
            return redirect('reg:register')

    

    return render(req,'register.html')

# def login(req):
#     if req.method == 'POST':
#         username = req.POST['username']
#         password = req.POST['password']

#         # Hash the provided password using MD5
#         hashed_password = md5_hash(password)

#         try:
#             user = Credential.objects.get(username=username, password=hashed_password)
#             return redirect('/',{"user":user})
#         except Credential.DoesNotExist:
#             messages.info(req, "Invalid User")
#             return redirect('reg:login')

#     return render(req, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the home page or any other page

        messages.info(request, "Invalid User")
        return redirect('reg:login')

    return render(request, 'login.html')