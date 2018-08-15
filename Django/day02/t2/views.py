from django.shortcuts import render
from .models import Commodity
# Create your views here.
def my_goods(req):
    data = Commodity.objects.filter(goods_price__gt=10)
    result = {
        "title":"商品",
        "array":data
    }
    return render(req,"goods.html",result)
def search_by_name(req):
    value = req.GET
    kw = value.get("kw")
    res = Commodity.objects.filter(
        goods_name__contains=kw
    )
    return render(req,"goods.html",{"array":res})


