from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=" عنوان دسته بندی ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="نویسنده")
    category = models.ManyToManyField(Category,related_name='articles',verbose_name="دسته بندی")
    title = models.CharField(max_length=200,verbose_name="عنوان")
    body = models.TextField(verbose_name="بدنه ی متن")
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,null=True)

    def get_absolute_url(self):
        return reverse("blog_app:article_detail", args=[self.id])

    class Meta:
        ordering = ['-created',]
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return format_html('<h3 style="color: red">تصویر وجود ندارد</h3>')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments',verbose_name="نویسنده")
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments',verbose_name="مقاله")
    body = models.TextField(max_length=500,verbose_name="بدنه کامنت")
    created = models.DateTimeField(auto_now_add=True,verbose_name="زمان ساخت")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='reply', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

class Message(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")
    email = models.EmailField(verbose_name="ایمیل")
    created = models.DateTimeField(auto_now_add=True,verbose_name="زمان ساخت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'



class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='likes',verbose_name='کاربر')
    article = models.ForeignKey(Article,on_delete=models.CASCADE , related_name='likes',verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} liked {self.article.title}'

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created_at',)