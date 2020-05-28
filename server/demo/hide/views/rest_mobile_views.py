from django.contrib.auth.decorators import login_required

from ..models import Myfile
from ..forms import MyfileForm
from . import myfile_views

from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required(login_url='rest_login')
def rest_get_myfile_list(request):
    myfiles = list(Myfile.objects.filter(author_id=request.user.id).values())
    # print(type(myfiles))
    # print(myfiles)
    new_dict = {'result': 'success'}
    new_dict['my_file_list']= myfiles

    if request.method == "POST":
        return JsonResponse(new_dict,
                            json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result': 'fail', 'message': 'use POST'}, json_dumps_params={'ensure_ascii': True})


@login_required(login_url='rest_login')
def rest_myfile_modify(request):
    if myfile_views.network_state_check(request.user)==False:
        return JsonResponse({'result': 'fail', 'message': 'PC is not connected'},
                            json_dumps_params={'ensure_ascii': True})

    # current_author_id, myfile_id
    if 'file_path' not in request.POST or 'state' not in request.POST:
        return JsonResponse({'result': 'fail', 'message': 'input file_path, state'},
                            json_dumps_params={'ensure_ascii': True})
    else:
        myfile = get_object_or_404(Myfile, file_path=request.POST['file_path'])

    if request.user.id != myfile.author_id:
        return JsonResponse({'result': 'fail', 'message': 'no authentication'},
                            json_dumps_params={'ensure_ascii': True})

    if request.method == "POST":
        form = MyfileForm(request.POST, instance=myfile)
        if form.is_valid():
            ## communicate with PC start


            ## communicate with PC end

            myfile = form.save(commit=False)
            myfile.state = request.POST['state']

            if myfile.validate_unique():
                messages.error(request, '수정할 수 없습니다')
                # return redirect('hide:index')
            else:
                myfile.save()
                return JsonResponse({'result':'success'},
                                    json_dumps_params={'ensure_ascii': True})
        else:
            return JsonResponse({'result': 'fail', 'message': 'invalid form'},
                                json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result': 'fail', 'message': 'use POST'},
                            json_dumps_params={'ensure_ascii': True})