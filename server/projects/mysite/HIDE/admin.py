from django.contrib import admin

from .models import Question

'''
Question 모델 내에서 제목(subject)으로 검색기능 추가
'''
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)