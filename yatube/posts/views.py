from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context)


# Страница с постами
def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)