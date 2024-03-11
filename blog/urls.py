from django.urls import path 
from .views import HomeView , PostNewView , PostDetailView , PostUpdateView , PostDeleteView , Post

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('post/new', PostNewView.as_view(), name= 'post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name= 'post_detail'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name= 'delete'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name= 'update'),
]