from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField('Загаловок', max_length=255)
    slug = models.SlugField('Ссылка', unique=True)
    image = models.ImageField('Картинка', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs= {'slug': self.slug})

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField('Загаловок', max_length=255)
    slug = models.SlugField('Ссылка', unique=True)
    image = models.ImageField('Картинка', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, blank=True, verbose_name='Категории')
    content = models.TextField('Текст')
    date = models.DateTimeField('Дата', default=timezone.now)
    publish = models.BooleanField('Опубликовано', default=False)
    views = models.IntegerField('Просмотры', default=0)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs= {'slug': self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Новость')
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата', default=timezone.now)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.user.username
