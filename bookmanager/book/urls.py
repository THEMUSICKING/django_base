# -*-coding:utf-8-*-
from django.contrib import admin
from django.urls import path
from book.views import index
urlpatterns = [
    path('index/',index)

]