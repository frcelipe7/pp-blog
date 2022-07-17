from django.shortcuts import render
from django.http import request
from .models import *

from markdown2 import Markdown


def index(request):
    return render(request, 'app_blog/home.html')


def devocional(request, id):
    devocional = createDevocional.objects.get(id=1)

    markdowner = Markdown()
    text_display = markdowner.convert(devocional.text)

    return render(request, 'app_blog/read.html', {
        'devocional': devocional,
        'text': text_display
    })


def adicionar(request):
    if request.method == "POST":
        theme = request.POST['theme']
        # image = request.FILE['image']
        verse = request.POST['verse']
        reference = request.POST['reference']
        text = request.POST['text']

        createDevocional(
            theme=theme,
            verse=verse,
            reference=reference,
            text=text
        ).save()
        return render(request, 'app_blog/adicionar.html', {
            'message': 'Devocional adicionado com sucesso!'
        })
    return render(request, 'app_blog/adicionar.html')
