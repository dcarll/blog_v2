from django.shortcuts import render
from .forms import ContatoForm
from django.core.mail import EmailMessage

# Create your views here.
def contato(request):
    send = True
    
    send = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('message')
        email = EmailMessage(
            "mensagem do blog django",
            "De {} <{}> Ecreveu: \n\n {}".format(nome, email, mensagem),
            "não-responder@inbox.mailtrap.io",
            ["dcarloss111@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False

        #enviar email
        
    
    context = {
        'form': form,
        'success':send,
    }

    return render(request, 'contato/contato.html', context)
