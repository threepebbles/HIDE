from django.shortcuts import render
#
# from django.http import HttpResponse
# import json
#
# def index(request):
#     response = {}
#     response['key'] = 'needs'
#     return HttpResponse(json.dumps(response), content_type="apllication/json")
#     # return render(request, 'hide/home.html')

from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse

# @api_view(('POST',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def index(request):
    # response = JsonResponse({"detail": "Hi home."},
    #                         status=status.HTTP_200_OK)
    #
    # return response
    return render(request, 'hide/home.html')