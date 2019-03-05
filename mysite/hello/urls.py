from django.urls import path
from .import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('post/' ,views.post, name='post' ),
    path('login/', views.login, name='login'),
    path('join/',views.join, name='join'),
    path('write/',views.write, name='write'),
    path('write/index/<int:pk>/',views.index, name="index"),
    path('write/index/<int:pk>/del/',views.delete,name="delete"),
    path('write/edit/<int:pk>/',views.edit, name='edit'),
    path('album/',views.crawl, name='crawl')
]