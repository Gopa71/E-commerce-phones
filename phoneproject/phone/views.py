from django.shortcuts import render
from .models import Category,Product
from django.shortcuts import get_object_or_404
# Create your views here.

def allProCat(req,c_slug=None):
    c_page=None
    if c_slug!=None:
       c_page=get_object_or_404(Category,slug=c_slug)
       product_list=Product.objects.filter(category=c_page,available=True)
    else:
       product_list=Product.objects.filter(available=True)
    return render(req,'category.html',{'product_list':product_list,'category':c_page})

def details(req,id):
   data=Product.objects.get(id=id)
   return render(req,'details.html',{'data':data})
   