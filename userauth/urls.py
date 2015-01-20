from django.conf.urls import patterns, url
from userauth import views

urlpatterns = patterns('',
    url(r'^register/', views.register, name = 'register'),
    url(r'^accounts/login/', views.user_login, name = 'login'),
    url(r'^accounts/logout/', views.logout_view, name = 'logout_view')
)