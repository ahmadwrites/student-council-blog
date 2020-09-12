from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('writings/', views.writings, name='blog-writings'),
    path('contact/', views.contact, name='blog-contact'),
    path('post/<slug:slug>/', views.details, name='blog-detail'),
    path('writings/<str:topic>/', views.topics, name='blog-topics')
]