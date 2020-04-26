from django.urls import path
from .views import post
from .views import error
from django.conf.urls import handler404

urlpatterns = [
    path('', post.post_list, name='post_list'),
    path('post/<int:pk>/', post.post_detail, name='post_detail'),
    path('post/addneu/', post.post_new, name='post_new'),
    path('post/<int:pk>/bearbeiten/', post.post_edit, name='post_edit'),
    path('post/<int:pk>/entfernen/', post.post_remove, name='post_remove'),
    path('kontakt', post.kontakt, name='kontakt'),
    path('home', post.home_list, name='home_list'),
    path('accounts/login/', error.forbidden, name='forbidden'),
    path('get404', error.get404, name='get404'),
]
handler404 = 'blog.views.error.handler404'