# shareRes > urls.py
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/',views.restaurantDetail),
    path('restaurantCreate/',views.restaurantCreate),
    path('restaurantCreate/create',views.Create_restaurant),
    path('categoryCreate/',views.categoryCreate, name="category"),
    path('categoryCreate/create',views.Create_category),
    path('categoryCreate/delete',views.Delete_category),
]
