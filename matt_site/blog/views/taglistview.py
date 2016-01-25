from django.views.generic import ListView

from blog.models.tag import Tag
from blog.models.article import Article

class TagListView(ListView):
    
    model = Tag
    template_name = 'blog/taglist.html'

    def get_queryset(self):
        return Tag.objects.prefetch_related('articles').order_by('tag')