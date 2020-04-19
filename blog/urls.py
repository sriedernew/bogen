from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/addneu/', views.post_new, name='post_new'),
    path('post/<int:pk>/bearbeiten/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/entfernen/', views.post_remove, name='post_remove'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('home', views.home_list, name='home_list'),
    path('accounts/login/', views.forbidden, name='forbidden'),
]