from django.shortcuts import render
from blog_app.models import Article
# Create your views here.
def home(request):
    articles = Article.objects.all()
    recent_article = Article.objects.all().order_by("-created",)
    return render(request,"home_app/index.html",{"articles":articles})