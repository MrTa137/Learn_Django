from django.contrib import admin
from django.conf.urls import url
from second_app import views
app_name="second_app"
urlpatterns = [
    url(r'^$', views.index, name="index" ),
    url(r'^danh_sach/$', views.danh_sach, name="danh_sach" ),
    url(r'^chi_tiet/$', views.chi_tiet, name="chi_tiet" ),
    url(r'^tin_tuc/$', views.tin_tuc, name="tin_tuc" ),
]
