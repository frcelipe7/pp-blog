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
import smtplib
import email.message


def send_email(devocional_theme, verse, referencia, devocional_id):
    all_users = newsLetter.objects.all()
    try:
        for user in all_users:
            username = f"{user.username.title()}"
            corpo_email = f"""
                <!DOCTYPE html>
                <html lang="pt-br">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                </head>
                <body>
                    <p>
                        Olá <b>{username}.</b> Nós acabamos de publicar
                        mais um estudo bíblico para a sua edificação espiritual. Da só
                        uma olhada:
                    </p> <br>
                    <section class="block" style="height: 100%;width: 100%;padding-top: 50px;display: flex; align-items: center;">
                        <div class="text-content" style="height: auto;width: 60%;background-color: #f8f8f8;border-radius: 5px 5px 0 0;padding: 70px 0;margin-bottom: 100px;border: 1px solid #C08D2C;border-top: 20px solid #C08D2C;box-shadow: 0 5px 1em #CBCBCB;">
                            <div class="text-title" style="width: 100%; font-size: 20pt; text-align: center; font-weight: 600;">{devocional_theme.upper()}</div>
                            <div class="verse-and-reference" style="width: 90%;height: auto;margin: auto;margin-top: 30px;margin-bottom: 50px;">
                                <div class="verse">
                                    <p style="font-style: italic;font-weight: 300;text-align: center;font-size: 17px;position: relative;">
                                        {verse}
                                    </p>
                                </div>
                                <div class="reference" style="text-align: center;font-size: 19px;">
                                    {referencia}
                                </div>
                            </div>
                            <div style="width: 100%; text-align: center;">
                                <a style="background-color: #C08D2C; padding:10px 15px; color: white; border-radius: 30px; margin: auto;" href="http://127.0.0.1:8000/devocional/id={devocional_id}">
                                    Leia mais clicando aqui!
                                </a>
                            </div>
                        </div>
                    </section>
                </body>
                </html>
            """

            msg = email.message.Message()
            msg['Subject'] = "Teste"
            msg['From'] = 'dev.testes.77@gmail.com'
            msg['To'] = f"{user.email}"
            password = 'lbksxwtnobkncfhi' 
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            with smtplib.SMTP('smtp.gmail.com: 587') as s:
                s.starttls()
                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                print("Email enviado")
    except:
        pass


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
            new_devocional = createDevocional(
                theme=theme,
                verse=verse,
                reference=reference,
                text=text
            )

            new_devocional.save()
            
            # Aqui eu tenho que adicionar o negócio pra
            # enviar email pro pessoal que ta inscrito
            # na Newsletter
            try:
                
                send_email(new_devocional.theme, new_devocional.verse, new_devocional.reference, new_devocional.id)
            except:
                return render(request, 'app_blog/adicionar.html', {
                    'error_message': 'Adicionado com erro no envio de email!'
                })

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


def newsletter(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['name']

        newsLetter(email=email, username=username.title()).save()

        return HttpResponseRedirect(reverse('index'))

    return render(request, 'app_blog/newsletter.html')
