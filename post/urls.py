from django.urls import path
from post.views import PostView, UserPostView

urlpatterns = [
    path('<int:post_id>/', PostView.as_view(), name='post'),
    path('create/', UserPostView.as_view(), name='create_post'),
]
