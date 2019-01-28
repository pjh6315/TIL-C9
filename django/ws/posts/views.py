from django.shortcuts import render
from .models import Post
# Create your views here.

def new(request):
    return render(request,'new.html')
    
def create(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    # DB INSERT
    post = Post(name=name,email=email,birthday=birthday,age=age)
    post.save()

    return render(request,'create.html')