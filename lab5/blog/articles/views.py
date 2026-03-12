# -*- coding: cp1251 -*-
# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404
from models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def create_post(request):
    if request.user.is_anonymous():
        raise Http404

    if request.method == "POST":
        # обработка отправленной формы
        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }
        errors = []

        # проверка заполненности полей
        if not form['title']:
            errors.append('Введите название статьи')
        if not form['text']:
            errors.append('Введите текст статьи')

        # проверка уникальности заголовка
        if form['title'] and Article.objects.filter(title=form['title']).exists():
            errors.append('Статья с таким названием уже существует')

        if not errors:
            # если ошибок нет, создаём статью
            article = Article.objects.create(
                title=form['title'],
                text=form['text'],
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            # возвращаем форму с ошибками
            return render(request, 'create_post.html', {'form': form, 'errors': errors})
    else:
        # GET-запрос: просто показываем пустую форму
        return render(request, 'create_post.html', {})
