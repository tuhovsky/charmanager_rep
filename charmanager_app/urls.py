from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$',
        views.view_all_usercharacters,
        name='view-all-usercharacters'),

    url(r'^(?P<usercharacter_id>[0-9]+)/$',
        views.usercharacter_detail,
        name='usercharacter-detail'),

    url(r'^register/$',
        views.register,
        name='register'),

    url(r'^accounts/login/$',
        login,
        name='login'),

    url(r'^accounts/logout/$',
        logout,
        name='logout'),
]
