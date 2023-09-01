
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/create/',views.create,name='create'),
    path('todo_list/',views.retreive,name='todo_list'),
    path('todo_list/update/<int:id>/',views.update,name='update'),
    path('todo_list/delete/<int:id>/',views.delete,name='delete'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register')

]
