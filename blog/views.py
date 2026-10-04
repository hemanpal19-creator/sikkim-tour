from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    # Fetch only published articles for the public Journal page.
    posts = Post.objects.filter(
        is_active=True
    ).order_by("-created_at")

    return render(
        request,
        "blog/list.html",
        {"posts": posts},
    )


def post_detail(request, slug):
    # Find one published article using its unique slug.
    post = get_object_or_404(
        Post,
        slug=slug,
        is_active=True,
    )

    return render(
        request,
        "blog/detail.html",
        {"post": post},
    )