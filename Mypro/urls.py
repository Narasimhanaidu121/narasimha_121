"""
URL configuration for Protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Mypro import views
app_name = 'Mypro'
urlpatterns = [
   path('home', views.home, name='home'),
   path('about', views.about, name='about'),
   path('blog', views.blog, name='blog'),
   path('blog_single', views.blog_single, name='blog_single'), #nn
   path('contact', views.contact, name='contact'),
   path('index', views.index, name='index'),
   path('portfolio', views.portfolio, name='portfolio'),
   path('portfolio1', views.portfolio1, name='portfolio1'),
   path('index3', views.index3, name='index3'),#???
   path('about1', views.about1, name='about1'),#????
   path('events', views.events, name='events'),
   path('contact1', views.contact1, name='contact1'),
   path('reservation1', views.reservation1, name='reservation1'),#??????
   path('rooms', views.rooms, name='rooms'),#???????????




   path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
   

]
    
