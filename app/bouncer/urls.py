"""
URL Mappings for Bouncer
"""

from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern

from bouncer import views


app_name = 'bouncer'

urlpatterns =[
    path('<str:slug>/', views.handle_redirect, name='redirect'),
    path('', views.landing, name='landing'),

]