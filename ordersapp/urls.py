from django.urls import path, include
from .views import Last

urlpatterns = [
 path('last/<int:clientid>/<int:days>/', Last.as_view(), name='last'),
]
