from django.conf.urls import patterns, url
from nasarover import views
from nasarover.views import RoverList, RoverDetail
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^newgrid/', views.newgrid, name='newgrid'),
    url(r'^senform/', views.senform, name='senform'),
    url(r'^process/', views.process, name='process'),
    url(r'^rover/$', views.RoverList.as_view()),
    url(r'^rover/(?P<pk>[0-9]+)/$', views.RoverDetail.as_view()),
)