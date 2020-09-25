from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views as user_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

path('', user_views.mainhome, name="mainhome"),
path('base_view', user_views.base, name="base"),
url(r'^business_api/',user_views.business_api.as_view()),

]

