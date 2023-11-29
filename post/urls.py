from django.urls import path

from post import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-post", views.create_post, name="new-post"),
]