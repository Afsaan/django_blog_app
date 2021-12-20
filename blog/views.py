from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author':'Afsan k',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'19 dec 2021'
    },
    {
        'author':'rahul T',
        'title':'blog post 2',
        'content':'Second post content',
        'date_posted':'21 dec 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})

