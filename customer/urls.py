from django.urls import path
from . import views

urlpatterns = [
    path('',views.chef,name='chef'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('order',views.order,name='order'),
    path('foods',views.foods,name='foods'),
    path('foodsearch',views.foodsearch,name='foodsearch'),
    path('contact',views.contact,name='contact'),
    path('categories',views.categories,name='categories'),
    path('categoryfoods',views.categoryfoods,name='categoryfoods')
    
]