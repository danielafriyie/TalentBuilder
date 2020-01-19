from django.shortcuts import render, get_object_or_404
from . import models


def blogs(request):
    context = {
        'blogs': models.Blog.objects.order_by('-id').all()
    }
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id, year, month, day, blog_title):
    detail_blog = models.Blog.objects.get(id=blog_id, date__year=year, date__month=month, date__day=day,
                                          slug_field=blog_title)
    context = {
        'blog': detail_blog
    }
    return render(request, 'blog/blog.html', context)
