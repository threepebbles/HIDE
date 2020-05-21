from rest_auth.views import LoginView
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status

# class CustomLoginView(LoginView):
#     def get_response(self):
#         serializer_class = self.get_response_serializer()
#
#         if getattr(settings, 'REST_USE_JWT', False):
#             data = {
#                 'user': self.user,
#                 'token': self.token
#             }
#             serializer = serializer_class(instance=data,
#                                           context={'request': self.request})
#         else:
#             serializer = serializer_class(instance=self.token,
#                                           context={'request': self.request})
#
#         response = Response(serializer.data, status=status.HTTP_200_OK)
#         if getattr(settings, 'REST_USE_JWT', False):
#             from rest_framework_jwt.settings import api_settings as jwt_settings
#             if jwt_settings.JWT_AUTH_COOKIE:
#                 from datetime import datetime
#                 expiration = (datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA)
#                 response.set_cookie(jwt_settings.JWT_AUTH_COOKIE,
#                                     self.token,
#                                     expires=expiration,
#                                     httponly=True)
#         return response