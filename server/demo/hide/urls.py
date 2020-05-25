from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import base_views, myfile_views
from .views import rest_pc_views, rest_mobile_views, rest_network_state_views

app_name = 'hide'

# router = routers.DefaultRouter()
# router.register(r'hide_list', views.Myfile_restful_main)

urlpatterns = [
    # URL 별칭
    path('', base_views.index, name='index'),
    path('myfile', base_views.myfile_list, name='myfile_list'),

    # myfile_views.py
    path('myfile/create/', myfile_views.myfile_create, name='myfile_create'),
    path('myfile/modify/<int:current_author_id>/<int:myfile_id>/', myfile_views.myfile_modify, name='myfile_modify'),
    path('myfile/delete/<int:current_author_id>/', myfile_views.myfile_delete, name='myfile_delete'),

    # rest_pc_views.py
    path('myfile/rest/create/', rest_pc_views.rest_myfile_create, name='rest_myfile_create'),
    path('myfile/rest/delete/', rest_pc_views.rest_myfile_delete, name='rest_myfile_delete'),

    # rest_mobile_views.py
    path('myfile/rest/get_list/', rest_mobile_views.rest_get_myfile_list, name='rest_get_myfile_list'),

    # rest_network_state_views.py
    path('myfile/rest/get_network_state/', rest_network_state_views.rest_get_network_state, name='rest_get_network_state'),
]
