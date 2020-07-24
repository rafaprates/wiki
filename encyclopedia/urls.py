from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entryPage"),
    path("wiki/<str:title>/edit", views.edit_existing_page, name="editPage"),
    path("new_page/", views.create_new_page, name="createNewPage"),
    path("random_page", views.select_random_page, name="randomPage")
]
