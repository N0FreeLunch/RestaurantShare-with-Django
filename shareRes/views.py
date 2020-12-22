from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here,
def index(request):
    # return HttpResponse("index")
    categories = Category.objects.all()
    category = {"categories" : categories}
    return render(request, 'shareRes/index.html',category)
def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')
def restaurantCreate(request):
    categories = Category.objects.all()
    content = {"categories" : categories}
    return render(request, 'shareRes/restaurantCreate.html', {"categories" : categories})
def categoryCreate(request):
    categories = Category.objects.all()
    content = {"categories" : categories}
    # return render(request, "shareRes/categoryCreate.html", content)
    return render(request, "shareRes/categoryCreate.html", {"categories" : categories})

def Create_category(request):
    categoryName = request.POST['categoryName']
    new_category  = Category(category_name = categoryName)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse(category_name)

def Delete_category(request):
    categoryId = request.POST["categoryId"]
    categories = Category.objects.get(id = categoryId)
    categories.delete()
    return HttpResponseRedirect(reverse('category'))


def Create_restaurant(request):
    resCategory = request.POST["resCategory"]
    resTitle = request.POST["resTitle"]
    resLink = request.POST["resLink"]
    resContent = request.POST["resContent"]
    resLoc = request.POST["resLoc"]
    new_restaurant  = Restaurant(category_id = resCategory, restaurant_name = resTitle, restaurant_link = resLink, restaurant_content = resContent, restaurant_keyword = resLoc)
    print(new_restaurant.__dict__)
    new_restaurant.save()
    # return HttpResponse(resCategory + resTitle + resLink + resContent + resLoc)
    return HttpResponseRedirect(reverse('index'))
