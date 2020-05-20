from django.urls import path

from . import views

app_name = 'hide'

urlpatterns = [
    # URL 별칭
    path('', views.index, name='home'),
]