from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.template import Template
from markdown import markdown

from blog.models.article import Article

class ArticleView(DetailView):
    
    template_name = 'blog/article.html'

    def get_object(self):
        article = get_object_or_404(Article.objects.select_related('body').prefetch_related('tags'), key=self.kwargs['key'])
        article.body_template = Template(markdown(article.body.body))
        return article