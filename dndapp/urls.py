from django.conf.urls import include, url
from django.contrib import admin
from dndapp import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.char_list),
    url(r'^dndapp/new/$', views.new_char, name='new_char'),
]