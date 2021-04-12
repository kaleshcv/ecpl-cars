
from django.urls import path
from .views import *

urlpatterns = [

    path('index',indexPage),
    path('webhook',webhook),

]
