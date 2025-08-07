from blog_app.models import Article, Category


def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')
    return {'recent_articles': recent_articles}

def category_list(request):
    category_list = Category.objects.all()
    return {'category_list': category_list}