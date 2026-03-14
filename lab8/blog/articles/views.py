# -*- coding: cp1251 -*-
# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def logout_view(request):
    logout(request)
    return redirect('archive')
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

def signup(request):
    if request.user.is_authenticated():
        return redirect('archive')

    if request.method == "POST":
        # обработка отправленной формы
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        errors = []

        # проверка заполненности
        if not username:
            errors.append('Введите имя пользователя')
        if not email:
            errors.append('Введите email')
        if not password:
            errors.append('Введите пароль')
        if password != password_confirm:
            errors.append('Пароли не совпадают')

        # проверка уникальности имени
        if username and User.objects.filter(username=username).exists():
            errors.append('Пользователь с таким именем уже существует')

        if not errors:
            # создаём пользователя
            user = User.objects.create_user(username, email, password)
            # сразу авторизуем
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'signup.html', {'errors': errors, 'form': request.POST})
    else:
        return render(request, 'signup.html', {})


def login_view(request):
    if request.user.is_authenticated():
        return redirect('archive')

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        errors = []

        if not username:
            errors.append('Введите имя пользователя')
        if not password:
            errors.append('Введите пароль')

        if not errors:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('archive')
                else:
                    errors.append('Аккаунт заблокирован')
            else:
                errors.append('Неверное имя пользователя или пароль')

        return render(request, 'login.html', {'errors': errors, 'form': request.POST})
    else:
        return render(request, 'login.html', {})
