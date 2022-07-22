from ast import keyword
from venv import create
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .models import *

from markdown2 import Markdown
import calendar
import locale


def index(request):
    devocionais = createDevocional.objects.order_by('-id')
    return render(request, 'app_blog/home.html', {
        'devocionais': devocionais
    })


def login_view(request):
    if request.method == 'POST':
        login_or_register = request.POST['method']
        if login_or_register == 'login':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "app_blog/login.html", {
                    "message_user": "Login e/ou senha inválidos."
                })
        elif login_or_register == 'register':
            pass
    else:
        return render(request, "app_blog/login.html")
    

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

# @login_required
def adicionar(request):
    print(request.user)
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("index"))
    if request.user.is_superuser == False:
        return HttpResponseRedirect(reverse("index"))
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


def search(request):
    keyword_search = request.GET.get("keyword_search", "")

    not_found = False

    all_devocionais = createDevocional.objects.all()

    return_devocionais = []

    for devocional in all_devocionais:
        if keyword_search.lower() in devocional.theme.lower():
            return_devocionais.append(devocional)
        elif keyword_search.lower() in devocional.reference.lower():
            return_devocionais.append(devocional)
        elif keyword_search.lower() in devocional.text.lower():
            return_devocionais.append(devocional)
    
    if return_devocionais.__len__() == 0:
        not_found = f'Não foram encontrados resultados para a pesquisa "{keyword_search}". Tente utilizar uma outra palavra-chave.'
    
    return render(request, 'app_blog/search.html', {
        'response': return_devocionais,
        "keyword_search": keyword_search,
        'not_found': not_found
    })


def devocionais(request):
    pass