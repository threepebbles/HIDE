from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import base_views, myfile_views
from .views import myfile_rest_views

app_name = 'hide'

# router = routers.DefaultRouter()
# router.register(r'hide_list', views.Myfile_restful_main)

urlpatterns = [
    # URL 별칭
    path('', base_views.index, name='index'),
    path('myfile', base_views.myfile_list, name='myfile_list'),
    # path('api-auth/', include(router.urls)),

    # myfile_views.py
    path('myfile/create/', myfile_views.myfile_create, name='myfile_create'),
    path('myfile/modify/<int:current_author_id>/<int:myfile_index>/', myfile_views.myfile_modify, name='myfile_modify'),
    path('myfile/delete/<int:current_author_id>/', myfile_views.myfile_delete, name='myfile_delete'),

    # myfile_rest_views.py
    path('myfile/rest/create/', myfile_rest_views.myfile_rest_create, name='myfile_rest_create'),
    path('myfile/rest/delete/', myfile_rest_views.myfile_rest_delete, name='myfile_rest_delete'),
]
