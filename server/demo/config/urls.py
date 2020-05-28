from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
from django.urls import include, path

from hide.views import base_views
from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),

    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('hide/', include('hide.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path

    path('chat/', include('chat.urls')),


    # 인증 관련
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('account/', include('allauth.urls')),
    # url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]

handler404 = 'common.views.page_not_found'