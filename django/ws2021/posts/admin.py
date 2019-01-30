from django.contrib import admin
from .models import Post, Comment, Question, Choice


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Choice)