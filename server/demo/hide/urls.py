from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'hide'

router = routers.DefaultRouter()
router.register(r'hide_list', views.HideList_restful_main)

urlpatterns = [
    # URL 별칭
    path('', views.index, name='hide_home'),
    path('api-auth/', include(router.urls))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)