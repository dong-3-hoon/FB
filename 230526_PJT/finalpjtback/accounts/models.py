from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=100)
    profile_image = models.ImageField(blank=True, null=True)

    # username 을 nickname에 자동으로 삽입
    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.username  # username 값을 nickname으로 복사
        super().save(*args, **kwargs)