
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout

app_name='accounts'

urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'^login/$' , login,{'template_name':'login.html'} , name='login'),
    url(r'^logout$' , logout),
    url(r'^signup$' , views.register , name='register'),

    url(r'^(?P<slug>[-\w]+)/$', views.profile, name='profile'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit_profile, name='edit_profile'),


    url(r'^(?P<slug>[-\w]+)/change_password$', views.change_password, name='change_password'),
]
