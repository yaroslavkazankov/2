from django.shortcuts import render

from .models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'articles': Article.objects.order_by(ordering).all()}
    # for article in context['articles']:
    #     all_article_scopes = ArticleScope.objects.filter(article__id=article[id])
        #same_all_items_with_breakfast_menu = breakfast.item_set.all()
    #    print (all_article_scopes)
    print(context)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
