from django.db import models
from django.contrib.auth.models import User

'''
Question 모델
'''
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # on_delete=models.CASCADE 옵션은 계정이 삭제되면 이 계정과 연결된 Question 데이터도 모두 삭제된다는 의미
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 사용자 구분
    def __str__(self):
        return self.subject

'''
Answer 모델
'''
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
