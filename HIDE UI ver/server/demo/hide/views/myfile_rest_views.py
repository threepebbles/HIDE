from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.db import models
from ..forms import MyfileForm
from ..models import Myfile

from django.http import HttpResponse, JsonResponse


@login_required(login_url='rest-auth:rest_register')
def myfile_rest_create(request):
    if request.method == 'POST':
        form = MyfileForm(request.POST)
        if form.is_valid():
            myfile = form.save(commit=False)
            myfile.author = request.user  # 추가한 속성 author 적용

            # (author, index) already exist
            if myfile.validate_unique():
                messages.error(request, '추가할 수 없습니다')
                # return redirect('hide:index')
            # create success
            else:
                myfile.save()
                return JsonResponse({'message': 'create success'}, json_dumps_params = {'ensure_ascii': True})

            # return redirect('hide:index')
    else:
        return JsonResponse({'message': 'use POST'}, json_dumps_params = {'ensure_ascii': True})


@login_required(login_url='rest-auth:rest_register')
def myfile_rest_delete(request):
    """
    hide 질문삭제
    """
    if request.method == 'POST':
        Myfile.objects.filter(author_id=request.user.id).delete()
        return JsonResponse({'message': 'delete success'}, json_dumps_params = {'ensure_ascii': True})
    else:
        return JsonResponse({'message': 'use POST'}, json_dumps_params={'ensure_ascii': True})

