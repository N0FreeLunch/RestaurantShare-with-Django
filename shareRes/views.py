from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here,
def index(request):
    # return HttpResponse("index")
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    data = {"categories" : categories, "restaurants": restaurants}

    # for record in data["categories"]:
    #     temp = []
    #     for record2 in restaurants:
    #         if record.id == record2.category_id:
    #             temp.append(record2)
    #     record.restaurants = temp
    #     print(record.__dict__)
    #     for record2 in record.restaurants:
    #         print(record2.__dict__)
    #     print("-------")

    return render(request, 'shareRes/index.html',data)

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    categories = Category.objects.all()
    data = {"title" : "맛집 상세보기", "categories" : categories, "restaurant": restaurant, "disabled" : "disabled"}
    return render(request, 'shareRes/restaurantCreate.html', data)

def restaurantUpdate(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    categories = Category.objects.all()
    data = {"title" : "맛집 수정하기", "categories" : categories, "restaurant": restaurant, "action" : "update"}
    return render(request, 'shareRes/restaurantCreate.html',data)

def restaurantCreate(request):
    categories = Category.objects.all()
    data = {"title" : "맛집 추가하기", "categories" : categories, "action" : "create"}
    return render(request, 'shareRes/restaurantCreate.html', data)

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

def Update_restaurant(request):
    resId = request.POST["resId"]
    resTitle = request.POST["resTitle"]
    resLink = request.POST["resLink"]
    resContent = request.POST["resContent"]
    resLoc = request.POST["resLoc"]

    restaurant = Restaurant.objects.get(id = resId)
    restaurant.restaurant_name = resTitle
    restaurant.restaurant_link = resLink
    restaurant.restaurant_content = resContent
    restaurant.res_keyword = resLoc
    restaurant.save()

    print(restaurant.__dict__)

    # restaurant = Restaurant.objects.get(id = res_id)
    return HttpResponseRedirect(reverse('index'))

def Delete_restaurant(request):
    resId = request.POST["resId"]
    restaurant = Restaurant.objects.get(id = resId)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))
