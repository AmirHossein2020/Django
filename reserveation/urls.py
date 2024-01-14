from django.urls import path
from . import views

app_name = "reserveation"


urlpatterns = [
    path("",views.reserve,name="reserve"),
]
