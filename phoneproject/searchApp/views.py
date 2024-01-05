from django.shortcuts import render
from phone.models import Product
from django.db.models import Q

# Create your views here.
def search(req):
    products=None
    quary=None
    if 'q' in req.GET:
        quary=req.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=quary))
       
    return render(req,'search.html',{'quary':quary,'products':products})