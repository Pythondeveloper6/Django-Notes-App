
from django.conf.urls import url
from . import views


app_name='home'

urlpatterns = [
    url(r'^$' , views.allnotes , name='all_notes'),
]
