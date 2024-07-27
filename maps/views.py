from django.http import HttpResponse

from .models import Shop, Product


def index(request):
    return HttpResponse("Hello, world. You're at the maps index.")

def getShops(request):
    shops = Shop.objects.all()
    return HttpResponse(shops)

def getProducts(request):
    products = Product.objects.all()
    return HttpResponse(products)


