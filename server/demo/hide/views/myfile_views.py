from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.db import models
from ..forms import MyfileForm
from ..models import Myfile


@login_required(login_url='common:login')
def myfile_create(request):
    """
    hide 질문등록
    """
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
                return redirect('hide:index')

            # return redirect('hide:index')
    else:
        form = MyfileForm()
    context = {'form': form}
    return render(request, 'hide/myfile_form.html', context)


@login_required(login_url='common:login')
def myfile_modify(request, current_author_id, myfile_index):
    """
    hide 질문수정
    """
    # myfile = Myfile.objects.filter(author_id=current_author_id, index=myfile_index)
    myfile = get_object_or_404(Myfile, index=myfile_index)
    
    if request.user != myfile.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('hide:index')

    if request.method == "POST":
        form = MyfileForm(request.POST, instance=myfile)
        if form.is_valid():
            myfile = form.save(commit=False)
            myfile.author = request.user

            # (author, index) already exist
            if myfile.validate_unique():
                messages.error(request, '수정할 수 없습니다')
                # return redirect('hide:index')
            # create success
            else:
                myfile.save()
                return redirect('hide:index')
    else:
        form = MyfileForm(instance=myfile)
    context = {'form': form}
    return render(request, 'hide/myfile_form.html', context)


@login_required(login_url='common:login')
def myfile_delete(request, current_author_id):
    """
    hide 질문삭제
    """

    Myfile.objects.filter(author_id=current_author_id).delete()
    return redirect('hide:index')
