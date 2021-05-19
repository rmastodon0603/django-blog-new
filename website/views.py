from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at')
    }
    return render(request, 'index.html', context=context)


def details(request, pk=None):
    context = {
        'post': Post.objects.get(pk=pk) if pk is not None else None
    }

    return render(request, 'details.html', context=context)
