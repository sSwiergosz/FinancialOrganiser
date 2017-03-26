from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'organizer'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', auth_views.login, {'template_name': 'organizer/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
]