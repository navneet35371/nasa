from django.conf.urls import patterns, url

from nasarover import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^newgrid/', views.newgrid, name='newgrid'),
    url(r'^senform/', views.senform, name='senform'),
    url(r'^process/', views.process, name='process'),
)