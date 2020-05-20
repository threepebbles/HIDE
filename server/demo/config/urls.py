from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
from django.urls import include, path

from hide import views

urlpatterns = [
    path('common/', include('common.urls')),
    path('hide/', include('hide.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path

    # 인증 관련
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]