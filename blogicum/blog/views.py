from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    template_name = 'blog/index.html'
    context = {
        'posts': reversed()
    }
    return render(request, template_name, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template_name = 'blog/detail.html'
    context = {}
    return render(request, template_name, context)


def category_posts(
        request: HttpRequest,
        category_slug: str) -> HttpResponse:
    template_name = 'blog/category.html'
    context = {
        'category_slug': category_slug
    }
    return render(request, template_name, context)
