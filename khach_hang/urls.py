from django.contrib import admin
from django.conf.urls import url
from khach_hang import views
app_name="khach_hang"
urlpatterns = [
    url(r'^dang_nhap/$', views.dang_nhap, name="dang_nhap" ),
   
]
