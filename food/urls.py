from django.urls import path
from food.views import *
app_name='something'

urlpatterns=[
    path('veg/',veg,name='veg'),
    path('nonveg/',nonveg,name='nonveg')
]