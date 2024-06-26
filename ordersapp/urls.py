from django.urls import path, include
from .views import Last, load_picture_form

urlpatterns = [
 path('last/<int:clientid>/<int:days>/', Last.as_view(), name='last'),
 path('load_picture_form/', load_picture_form, name='load_picture_form')
]
