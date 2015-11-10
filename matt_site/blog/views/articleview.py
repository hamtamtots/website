from django.views.generic import DetailView
from markdown import markdown

from blog.models.article import Article

class ArticleView(DetailView):
    
    model = Article
    template_name = 'blog/index.html'

    def get_object(self):
        article = super().get_object()
        article.body = markdown(article.body)
        return article