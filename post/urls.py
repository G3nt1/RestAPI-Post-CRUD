from django.urls import path

from post import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-post", views.create_post, name="new-post"),
    path("delete-post", views.delete_post, name="delete-post"),
    path("get-post", views.get_post, name="get-post"),
    path("update-post", views.update_post, name="update-post"),
]