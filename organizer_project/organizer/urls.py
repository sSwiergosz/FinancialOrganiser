from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'organizer'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', auth_views.login, {'template_name': 'organizer/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^add/transaction/$', views.add_transaction, name='add_transaction'),
    url(r'^transactions/all/$', views.all_transactions, name='all_transactions'),
    url(r'^statistics/all/$', views.statistics, name='statistics')
]