from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Article, Category, Comment, Message, Like
from django.core.paginator import Paginator
from .forms import MessageForm


# Create your views here.
def articles_delails(request, slug):
    article = get_object_or_404(Article, slug=slug)

    # همیشه بررسی کن که کاربر وارد شده باشه
    if request.user.is_authenticated:
        is_like = request.user.likes.filter(article__slug=slug).exists()
    else:
        is_like = False

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, author=request.user, parent_id=parent_id)

    return render(request, "blog_app/article_detail.html", context={"article": article , "is_like": is_like})



def all_blog(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "blog_app/blog.html", {"articles": object_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog_app/blog.html", {"articles": articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "blog_app/blog.html", {"articles": object_list})


def contact(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            Message.objects.create(title=title, email=email, text=text)
    else:
        form = MessageForm()
    return render(request, "blog_app/contact_us.html", {"form": form})


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
    return redirect("blog_app:article_detail", slug)
