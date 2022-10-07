from django.urls import path
from app7.views import *
app_name='srikanth'
urlpatterns=[
    path('third/',third,name='third')
]