import random
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, FileResponse


# Create your views here.
from django.shortcuts import render

from .models import Student, Blog


def hello_view(request):
    blog_posts = Blog.objects.all()
    context = {'posts': blog_posts}
    return render(request, 'index.html', context)


def date_view(request):
    today = datetime.now()
    return HttpResponse(f"Now {str(today)}")


def random_number(request):
    num = random.randint(1, 1000)
    num2 = random.randint(1, num)
    num3 = random.randint(1, num2)
    num4 = random.randint(1, num3)
    context = {'num': num, 'numbers': [num2, num3, num4]}
    return render(request, 'random.html', context)


def image_view(request):
    path = settings.BASE_DIR / 'static' / '123.jpg'
    file = open(path, 'rb')
    return FileResponse(file)


def student_view(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def create_post(request):
    if request.method == "POST":
        form = request.POST
        title = form['title']
        description = form['description']
        hashtag = form['hashtag']
        image = request.FILES['image']
        Blog.objects.create(title=title, description=description, hashtags=hashtag, image=image)
        return HttpResponse("Blog post created successfully!")
    if request.method == "GET":
        return render(request, "create-post.html")
