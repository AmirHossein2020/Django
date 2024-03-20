from django.urls import path
from .views import SignUpView , ContactView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('contact/', ContactView.as_view(), name= 'contact'),
]