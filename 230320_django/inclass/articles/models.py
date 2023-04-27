from django.db import models

# Create your models here.
# Model 클래스를 상속받음
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 날짜
    updated_at = models.DateTimeField(auto_now=True)
    # 디버깅시 프린트 찍어주면 좋음
    def __str__(self):
        return f'{self.id}번째 - {self.title}'