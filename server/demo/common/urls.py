from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='common/logout.html'), name='logout'),
    path('signup/', auth_views.LoginView.as_view(template_name='common/signup.html'), name='signup'),
    path('email_verification/', auth_views.LoginView.as_view(template_name='common/email_verification.html'), name='email_verification'),
    path('password_reset/', auth_views.LoginView.as_view(template_name='common/password_reset.html'),
         name='password_reset'),
    path('password_reset_confirm/', auth_views.LoginView.as_view(template_name='common/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_change/', auth_views.LoginView.as_view(template_name='common/password_change.html'),
         name='password_change'),
]
