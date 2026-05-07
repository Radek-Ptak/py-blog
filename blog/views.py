from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


def index(request):
    post_list = (Post.objects
                 .select_related("owner")
                 .all()
                 .order_by("-created_time")
                 )

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "post_count": post_list.count(),
        "num_visits": num_visits + 1,
    }

    return render(
        request, "blog/index.html", context=context
    )


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects
                .select_related("owner")
                .prefetch_related("comments__user")
                )


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/commentary_form.html"
