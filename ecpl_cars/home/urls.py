
from django.urls import path
from .views import *

urlpatterns = [

    path('',indexPage),
    path('about-us',aboutUs),
    path('customer-service',customerService),
    path('parts-request',partRequest),
    path('webhook',webhook),
    path('find-parts',findParts),
    path('thanks-page',thanksPage),
    path('hub-test',hubspotTest),


]
