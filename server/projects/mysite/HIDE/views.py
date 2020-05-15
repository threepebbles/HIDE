from django.shortcuts import render
from .models import Question
from .forms import QuestionForm,  AnswerForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

'''
목록 출력
'''
def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'HIDE/question_list.html', context)

'''
HIDE 내용 출력
'''
def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # 존재하지 않는 데이터를 요청할 경우 500 오류페이지 대신 404 오류페이지를 출력하도록 detail 함수를 수정
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'HIDE/question_detail.html', context)

'''
answer 등록 (로그인 필요)
'''
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)

            answer.author = request.user  # 추가한 속성 author 적용

            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('HIDE:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'HIDE/question_detail.html', context)

'''
question 등록 (로그인 필요)
'''
@login_required(login_url='common:login')
def question_create(request):
    """
    HIDE 질문등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)

            question.author = request.user  # 추가한 속성 author 적용

            question.create_date = timezone.now()
            question.save()
            return redirect('HIDE:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'HIDE/question_form.html', context)