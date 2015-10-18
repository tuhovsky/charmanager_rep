from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_all_usercharacters,
        name='view-all-usercharacters'),

    url(r'^(?P<usercharacter_id>[0-9]+)/$',
        views.usercharacter_detail,
        name='usercharacter-detail'),

    url(r'^register/$', views.register,
        name='register')

]
