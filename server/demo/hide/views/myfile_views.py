from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import MyfileForm, NetworkStateForm
from ..models import Myfile, NetworkState


@login_required(login_url='common:login')
def myfile_create(request):
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
                return redirect('hide:myfile_list')

            # return redirect('hide:index')
    else:
        form = MyfileForm()
    context = {'form': form}
    return render(request, 'hide/myfile_form.html', context)


@login_required(login_url='common:login')
def myfile_modify(request, current_author_id, myfile_id):
    myfile = get_object_or_404(Myfile, id=myfile_id)

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
                return redirect('hide:myfile_list')
    else:
        form = MyfileForm(instance=myfile)
    context = {'form': form}
    return render(request, 'hide/myfile_form.html', context)


@login_required(login_url='common:login')
def myfile_delete(request, current_author_id):
    Myfile.objects.filter(author_id=current_author_id).delete()
    return redirect('hide:myfile_list')


def network_state_check(current_user):
    my_network_state = NetworkState.objects.filter(author=current_user)
    if len(my_network_state)==0:
        network_state_modify(current_user, "False")
        # print("network state created")
    # else:
        # print("network state already exists")
    return list(NetworkState.objects.filter(author=current_user))[0].network_state


def network_state_modify(current_user, state):
    form = NetworkStateForm()
    ns = form.save(commit=False)
    ns.author = current_user
    ns.network_state = state
    ns.save()
