from django.urls import path

from .views import (
    index,
    PostDetailView,
    CommentaryCreateView,
)

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("commentary/create",
         CommentaryCreateView.as_view(),
         name="commentary-create"
         ),
]
