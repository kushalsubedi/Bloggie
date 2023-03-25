from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create',views.create_Blog,name='create'),
    path('blog_detail/<int:pk>',views.blog_detail,name='blog_detail'),
    path('update_blog/<int:pk>',views.update_blog,name='update_blog'),
    path('delete_blog/<int:pk>',views.delete_blog,name='delete_blog')
]