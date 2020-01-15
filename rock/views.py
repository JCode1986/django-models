from django.views.generic import ListView, DetailView
from .models import Post

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
