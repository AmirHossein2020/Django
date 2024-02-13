from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path("register/",views.RegisterView.as_view(),name="register"),
]
