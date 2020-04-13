from django.urls import path, include
from .import views
from rest_framework import routers
app_name='languages'

routers =routers.DefaultRouter()
routers.register('languages', views.Languageview)


urlpatterns=[
    path('',include(routers.urls))
]