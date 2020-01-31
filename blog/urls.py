from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    #Want to be clear with naming of path
    #RegExp were used in older versions of Django
    path('about/', views.about, name='blog-about'),

]