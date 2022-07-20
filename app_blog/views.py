from django.shortcuts import render
from django.http import request
from .models import *

from markdown2 import Markdown
import calendar
import locale


def index(request):
    devocionais = createDevocional.objects.order_by('-id')
    return render(request, 'app_blog/home.html', {
        'devocionais': devocionais
    })


def devocional(request, id):
    devocional = createDevocional.objects.get(id=id)

    date = str(devocional.timestamp).split()[0].split('-')
    year = date[0]
    month = date[1]
    day = date[2]

    locale.setlocale(locale.LC_ALL, 'pt_BR') # pra traduzir o mês do ingles pro portugues

    month_name = calendar.month_name[int(month)] # pra pegar o nome do mês a partir do número

    date = f"{day} de {month_name} de {year}."

    markdowner = Markdown()
    text_display = markdowner.convert(devocional.text)

    return render(request, 'app_blog/read.html', {
        'devocional': devocional,
        'text': text_display,
        'date': date
    })


def adicionar(request):
    if request.method == "POST":
        theme = request.POST['theme']
        # image = request.FILE['image']
        verse = request.POST['verse']
        reference = request.POST['reference']
        text = request.POST['text']

        if theme == "" or verse == "" or reference == "" or text == "":
            return render(request, 'app_blog/adicionar.html', {
                'error_message': 'Nenhuma informação deve ser deixada em branco!',
                'text': text
            })
        try:
            createDevocional(
                theme=theme,
                verse=verse,
                reference=reference,
                text=text
            ).save()
            return render(request, 'app_blog/adicionar.html', {
                'message': 'Devocional adicionado com sucesso!'
            })
        except:
            return render(request, 'app_blog/adicionar.html', {
                'error_message': 'Ocorreu algum erro!'
            })
    return render(request, 'app_blog/adicionar.html')
