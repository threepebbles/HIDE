from django.urls import path

from .views import base_views, myfile_views
from .views import rest_pc_views, rest_mobile_views, rest_network_state_views

app_name = 'hide'

urlpatterns = [
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
