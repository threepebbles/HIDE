from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('hide/', include('hide.urls')),
    path('', TemplateView.as_view(template_name="base.html"), name='root'),  # '/' 에 해당되는 path

    # 인증 관련
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),

    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]