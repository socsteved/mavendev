from django.urls import path
from .views import *
urlpatterns = [
    path('',HomePageView.as_view(), name ='home'),
    path('cx/',CXPageView.as_view(), name = 'cx'),
    path('dq/',DQPageView.as_view(), name = 'dq'),
    path('send/',SendPageView.as_view(), name = 'send'),
    path('industry/',IndustryPageView.as_view(), name = 'indsol'),
    path('hx/',HXPageView.as_view(), name = 'hx'),
]
