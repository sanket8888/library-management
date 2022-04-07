from django.urls import path
from .views import *


urlpatterns = [
    path('home',index,name="home"),
    path('add/',add_books, name="add"),
    path('view/',view_books, name="view"),
    path('delete/<int:id>',delete_books, name="delete"),
    path('update/<int:id>',upd_books, name="update"),
]

