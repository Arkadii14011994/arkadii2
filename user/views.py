from django.shortcuts import render,redirect
from .models import ContactUS
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

    
def about(request):
    return render(request, 'about.html')

def client(request):
    return render(request, 'client.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')
    


def comment(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email= form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            messages = form.cleaned_data['message']
            try:
                subject = f'Добро пожаловать в наш магазин '
                message = f'Спасибо, что связались с нами {name} \n Ваш принят, в ближайшее время с вами свяжутся!'
                email_from = settings.EMAIL_HOST_USER
                recipient_list=[email]
                send_mail(subject, message, email_from, recipient_list, phone)
                ContactUS.objects.create(name=name, email=email, phone=phone, message=messages).save()
            except BadHeaderError:
                return HttpResponse('invalid data')
        return redirect('/')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context=context)







