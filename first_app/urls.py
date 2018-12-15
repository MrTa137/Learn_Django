from django.contrib import admin
from django.conf.urls import url
from first_app import views
app_name="first_app"
urlpatterns = [
    url(r'^tao/$', views.tao_cookie, name="tao" ),
    url(r'^doc/$', views.doc_cookie, name="doc" ),
    url(r'^xoa/$', views.xoa_cookie, name="xoa" ),
]
