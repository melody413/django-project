from django.urls import path, re_path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('crud/', views.crudops, name='crud'),
    path('dataman/', views.datamanipulation, name='datama'),
    re_path(r'^sendmail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.sendSimpleEmail, name='sendmail'),
]