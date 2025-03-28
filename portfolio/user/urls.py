from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.indexpage, name='index'),
    path('contact/', views.contactpage,name='contact'),
 ]