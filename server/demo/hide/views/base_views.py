import logging

from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Myfile, NetworkState

logger = logging.getLogger('hide')

def index(request):
    return render(request, 'hide/home.html')


def myfile_list(request):
    page = request.GET.get('page', '1')  # 페이지

    myfile_list = Myfile.objects.order_by('-id')
    network_state_list = NetworkState.objects.filter(author_id=request.user.id)

    # 페이징처리
    paginator = Paginator(myfile_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'myfile_list': page_obj, 'network_state_list': network_state_list,
               'page': page}

    return render(request, 'hide/myfile_list.html', context)
