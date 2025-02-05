import datetime as dt
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Category, Post


CURRENT_TIME = dt.datetime.now()


def index(request: HttpRequest) -> HttpResponse:
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
            'category',
            'location'
        ).filter(
            pub_date__lte=CURRENT_TIME,
            is_published=True,
            category__is_published=True
        ).order_by('-pub_date', )[:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=id,
        pub_date__lt=CURRENT_TIME,
        is_published=True,
        category__is_published=True
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(
        request: HttpRequest,
        category_slug: str) -> HttpResponse:
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = get_list_or_404(
        Post.objects.select_related(
            'category',
            'location'
        ).filter(
            category=category,
            pub_date__lt=CURRENT_TIME,
            is_published=True,
        )
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
