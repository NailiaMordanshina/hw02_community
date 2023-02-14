from django.shortcuts import render, get_object_or_404

from .models import Post, Group

#from yatube.settings import NUMBER_OF_POSTS


def index(request):
    template = 'posts/index.html'
    #posts = Post.objects.order_by('-pub_date')
    posts = Post.objects.all()[:10]


    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    #posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    #posts = Post.objects.filter(group=group).all()[10]
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'title': f'Записи сообщества {group}',
        'posts': posts,
    }
    return render(request, template, context)
