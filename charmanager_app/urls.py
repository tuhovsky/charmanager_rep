from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [

    url(r'^accounts/login/$',
        login,
        name='login'),

    url(r'^accounts/logout/$',
        logout,
        name='logout'),

    url(r'^accounts/register/$',
        views.register,
        name='register'),

    url(r'^usercharacters-list/$',
        views.usercharacters_list,
        name='usercharacters-list'),

    url(r'^(?P<usercharacter_id>[0-9]+)/$',
        views.usercharacter_detail,
        name='usercharacter-detail'),

]
