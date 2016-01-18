from django.views.generic import ListView

from blog.models.article import Article

class TaggedArticleListView(ListView):
    
    template_name = 'blog/list.html'

    def get_queryset(self):
        return Article.objects.filter(tags__tag=self.kwargs['tag'])

    def get_title(self):
        return 'Tagged \'{0}\''.format(self.kwargs['tag']);