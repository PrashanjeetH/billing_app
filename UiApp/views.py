from django.shortcuts import render, redirect, reverse
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {
        "body":"This is body from index page"
    }
    return render(request, 'UiApp/index.html', context)


def login(request):
    # print(request.csrftoken)
    print(f"{reverse('auth-user') = }")
    url = (str(request.build_absolute_uri(reverse('auth-user'))))
    # TODO: Collect username and password from the frontend
    if request.method == 'POST':
        print(f"{request = }")
        print(f"{request.POST = }")
        data = requests.post(url, request.POST), 
        json_data = data[0].json()
        context = {
            "body":"This is body from login page",
            "data": json_data
        }
        return render(request, 'UiApp/login.html', context)
    return render(request,  'UiApp/login.html', context={
        'body':'This is from get response'
    })


def post(request):
    context = {
        "body":"This is body from post page"
    }
    return render(request, 'UiApp/post.html', context)


def timeline(request):
    context = {
        "body":"This is body from timeline page"
    }
    return render(request, 'UiApp/posts.html', context)


@login_required(login_url='login')
def profile(request):
    context = {
        "body":"This is body from profile page"
    }
    return render(request, 'UiApp/profile.html', context)


@login_required(login_url='login')
def my_posts(request):
    context = {
        "body":"This is body from my-posts page"
    }
    return render(request, 'UiApp/posts.html', context)