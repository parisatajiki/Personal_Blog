from django.urls import path
from . import views


app_name = 'blog_app'
urlpatterns = [
    path('detail/<slug:slug>', views.articles_delails, name='article_detail'),
    path('', views.all_blog, name='all_articles'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),

]
