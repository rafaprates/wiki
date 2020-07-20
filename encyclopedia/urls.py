from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entryPage"),
    path("new_page/", views.createNewPage, name="createNewPage"),
    path("random_page", views.randomPage, name="randomPage")
]
