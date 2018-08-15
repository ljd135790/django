from django.http import HttpResponse
from django.shortcuts import render
from .models import FireCart
# Create your views here.
def my_carts(req):
    data = FireCart.objects.filter(speed__lt=300).order_by("speed")
    result = {
        "title":"火车",
        "carts":data
    }
    return render(req,"trains.html",result)
def search_by_name(req):
    param = req.GET
    kw = param.get("kw")
    res = FireCart.objects.filter(
        name__contains=kw
    )
    return render(req,"trains.html",{"carts":res})