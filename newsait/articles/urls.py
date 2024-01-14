from django.urls import path
from .views import (ArticleDeleteView,  ArticleCreateView)

from . import views

urlpatterns = [
    path("delete/<int:pk>/",ArticleDeleteView.as_view(),name="article_delete"),
    path("new/",ArticleCreateView.as_view(),name="article_create"),
    path("<int:pk>/edit/",views.article_update,name="article_update"), 
    path("<int:pk>/",views.article_detail,name="article_detail"),
    path("",views.arttile_list,name="article_list"),
]

#class
""" path("",ArticleListView.as_view(),name="article_list"), """
""" path("<int:pk>/",ArticleDetailView.as_view(),name="article_detail"), """
""" path("edit/<int:pk>/",ArticleUpdateView.as_view(),name="article_update"), """