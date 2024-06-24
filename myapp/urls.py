from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('coin/', views.coin, name='coin'),
 path('random_roll/', views.random_roll, name='random_roll'),
 path('random_number/', views.random_number, name='random_number'),
 path('glav/', views.glav, name='glav'),
 path('aboutme/', views.aboutme, name='aboutme'),
 #path('flipcoinlast/', views.FlipCoinLast, name='FlipCoinLast'),
 #path('test/', include('myapp.urls'))
]
