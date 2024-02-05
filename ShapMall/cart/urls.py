# در اینجا هم ادرس ویوی که درست کردیم میدیم
# تا جنگو با این ادرس ویوی مارو نشون بده
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', cart_summary, name='cart_summary'),
    path('add/', cart_add, name='cart_add'),
    path('delete/', cart_delete, name='cart_delete'),
    path('update/', cart_update, name='cart_update'),
]