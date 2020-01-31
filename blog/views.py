from django.shortcuts import render
#from django.http import HttpResponse

# ^We used the above when we were rendeirng the html directly here

# Dummy data- list of dictionary of posts

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    # ref subdirectory in templates
    return render(request, 'blog/home.html', context)


def about(request):
    # ref subdirectory in templates
    return render(request, 'blog/about.html', {'title': 'About'})
