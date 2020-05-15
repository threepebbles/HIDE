from django.urls import path

from . import views

# URL 네임스페이스
app_name = 'HIDE'

urlpatterns = [
    # path('', views.index),
    # path('<int:question_id>/', views.detail), # http://localhost:8000/HIDE/<int:question_id>/로 매핑
    # URL 별칭
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # HIDE/answer/create/2와 같은 페이지를 요청하면 views.answer_create함수를 호출하라는 매핑
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # HIDE/question/create 페이지를 요청하면 views.question_create 함수 호출
    path('question/create/', views.question_create, name='question_create'),
]