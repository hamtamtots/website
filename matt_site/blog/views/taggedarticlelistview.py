from blog.views.articlelistview import ArticleListView
from blog.models.article import Article

class TaggedArticleListView(ArticleListView):

    def get_queryset(self):
        return super().queryset.filter(tags__tag = self.get_tag_arg())

    def get_title(self):
        return 'Tag \'{0}\''.format(self.get_tag_arg());

    def get_tag_arg(self):
        return self.kwargs['tag']