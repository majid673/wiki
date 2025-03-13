from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # صفحه اصلی
    path("wiki/<str:title>", views.entry, name="entry"),  # نمایش مقاله
    path("search/", views.search, name="search"),  # جستجو
    path("new/", views.new_page, name="new_page"),  # ایجاد مقاله جدید
    path("random/", views.random_page, name="random_page"),  # مقاله تصادفی
    path("wiki/edit/<str:title>", views.edit_page, name="edit_page"),  # ویرایش مقاله
]









