from django.db import models


# Create your models here.


class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)  # 문자열이 들어갈 것을 말하고 최대 길이를 255로 지정
