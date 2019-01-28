from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
# 1. Create
# post = Post(title = 'Hello', content = 'world!')
# post.save()

# 2. Read
# 2.1 ALL
# posts = Post.objects.all()
# 2.2 Get one
# post = Post.objects.get(pk=1)
# 2.3 filter (WHERE)
# post = Post.objects.get(pk=1)
# post = Post.objects.filter(title='Hello').first()
# posts = Post.objects.filter(title='Hello').all()
# 2.4 LIKE
# posts = Post.objects.filter(title__contains='He').all()
# 2.5 order_by (정렬)
# posts = Post.objects.order_by('title').all()
# posts = Post.objects.order_by('-title').all()
# 2.6 limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]

# 3. delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.title = 'hi'
# post.save()