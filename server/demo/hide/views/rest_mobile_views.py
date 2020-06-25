from django.contrib.auth.decorators import login_required

from ..models import Myfile
from ..forms import MyfileForm
from . import myfile_views

from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@login_required(login_url='rest_login')
def rest_get_myfile_list(request):
    myfiles = list(Myfile.objects.filter(author_id=request.user.id).values())
    new_dict = {'result': 'success'}
    new_dict['my_file_list']= myfiles

    if request.method == "POST":
        return JsonResponse(new_dict,
                            json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result': 'fail', 'message': 'use POST'},
                            rjson_dumps_params={'ensure_ascii': True})