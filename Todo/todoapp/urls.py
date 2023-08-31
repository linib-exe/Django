
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('todo_list/',views.retreive,name='todo_list'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]
