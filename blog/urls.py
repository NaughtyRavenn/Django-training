from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path("", views.postListView.as_view(), name="blog"),
    path("<int:pk>/", views.postDetailView.as_view(), name="post"),
]
