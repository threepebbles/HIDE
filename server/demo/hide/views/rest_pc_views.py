from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..forms import MyfileForm
from ..models import Myfile

from django.http import JsonResponse

@login_required(login_url='rest_login')
def rest_myfile_create(request):
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
                return JsonResponse({'result':'success', 'message': 'create success'},
                                    json_dumps_params = {'ensure_ascii': True})
        else:
            return JsonResponse({'result':'fail', 'message': 'form is not valed'},
                                json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result': 'fail', 'message': 'use POST'},
                            json_dumps_params = {'ensure_ascii': True})


@login_required(login_url='rest_login')
def rest_myfile_delete(request):
    if request.method == 'POST':
        Myfile.objects.filter(author_id=request.user.id).delete()
        return JsonResponse({'result': 'success', 'message': 'delete success'},
                                json_dumps_params={'ensure_ascii': True})
    else:
        return JsonResponse({'result':'fail', 'message': 'use POST'},
                            json_dumps_params={'ensure_ascii': True})

