from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# News Story Model
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()

    class Meta:
        verbose_name_plural='News Stories'

    def __str__(self):
        return self.title