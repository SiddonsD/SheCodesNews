from django.contrib import admin
from .models import NewsStory

class AdminNewsStories(admin.ModelAdmin):
    list_display=('title', 'pub_date')

class AdminComment(admin.ModelAdmin):
    list_display=('news_story', 'comment_date_time', 'comment', 'status')
