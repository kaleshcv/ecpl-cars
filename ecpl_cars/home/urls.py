
from django.urls import path
from .views import *

urlpatterns = [

    path('index',indexPage),
    path('webhook',webhook),
    path('find-parts',findParts),
    path('thanks-page',thanksPage),
    path('hub-test',hubspotTest),

]
