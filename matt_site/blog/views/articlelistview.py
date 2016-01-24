from django.views.generic import ListView

from blog.models.article import Article

class ArticleListView(ListView):
    
    model = Article
    template_name = 'blog/articlelist.html'