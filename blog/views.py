# articles/views.py
from django.views.generic import ListView, DetailView
from .models import Article

# blog lists
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'


# blog details
class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'blog/article_detail.html'