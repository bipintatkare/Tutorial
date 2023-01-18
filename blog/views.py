from django.shortcuts import render, redirect
from .models import Blog
from django.views.decorators.csrf import csrf_exempt


def index(request):
    blogs = Blog.objects.all()
    return render(request, "homepage.html", {"blogs": blogs})


@csrf_exempt
def create_form(request):
    if request.method == "GET":
        return render(request, "blog-create.html")

    elif request.method == "POST":

        title = request.POST["title"]
        description = request.POST["description"]

        Blog.objects.create(
            title = title,
            description = description
        )

        return redirect("index")