
from django.urls import path
from .views import index,comment, about,product,client,contact


urlpatterns = [
    path('', index),
    path('about',about, name='about'),
    path('product',product,name='product'),
    path('client',client,name='client'),
    path('contact',contact,name='contact'),
    path('add_comment',comment,name = 'add_comment'),
    
]