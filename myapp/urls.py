from django.urls import path
from myapp import views

urlpatterns=[
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create/', views.create_task),
] 