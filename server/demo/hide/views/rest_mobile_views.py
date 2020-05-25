from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.db import models
from ..forms import NetworkStateForm, MyfileForm
from ..models import Myfile

from django.http import JsonResponse

@login_required(login_url='rest-auth:rest_register')
def rest_get_myfile_list(request):
    myfiles = list(Myfile.objects.filter(author_id=request.user.id).values())
    # print(type(myfiles))
    # print(myfiles)
    new_dict = {'result': 'success'}
    for i in range(len(myfiles)):
        new_dict[str(i)] = myfiles[i]

    if request.method == "POST":
        return JsonResponse(new_dict,
                            json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result': 'fail', 'message': 'use POST'}, json_dumps_params={'ensure_ascii': True})

