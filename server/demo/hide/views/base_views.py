import logging

from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Myfile

logger = logging.getLogger('hide')


def index(request):
    """
    hide 목록 출력
    """

    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    myfile_list = Myfile.objects.order_by('-index')
    context = {'myfile_list': myfile_list}

    # 검색
    if kw:
        myfile_list = myfile_list.filter(
            Q(file_path__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 글쓴이검색
            Q(state__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(myfile_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'myfile_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'hide/myfile_list.html', context)
