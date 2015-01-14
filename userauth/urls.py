from django.conf.urls import patterns, url
from userauth import views

urlpatterns = patterns('',
    url(r'^register/', views.register, name = 'register'),
    url(r'^login/', views.user_login, name = 'login'),
    url(r'^logout/', views.logout_view, name = 'logout_view')
)