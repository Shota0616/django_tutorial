import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # __str__ メソッド
    def __str__(self):
        return self.question_text

    # 公開日時（pub_date）が1日以内のものを返す
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # on_delete=models.CASCADE:関連するモデルもすべて削除する。外部キー
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # __str__ メソッド
    def __str__(self):
        return self.question_text