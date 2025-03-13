from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("wiki/<str:title>", views.entry, name="entry"),  # View article
    path("search/", views.search, name="search"),  # Search
    path("new/", views.new_page, name="new_page"),  # Create a new article
    path("random/", views.random_page, name="random_page"),  # Random article
    path("wiki/edit/<str:title>", views.edit_page, name="edit_page"),  # Article editing
]









