from django.shortcuts import render
from .forms import ContactForm
from .models import Projects
# from django.core.mail import send_mail
# Create your views here.

def home(request):
    context = {
        'projects':Projects.objects.all(),
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comments = form.cleaned_data['comments']
            form.save()

            # send_mail(
            #     f'{name}, Sent a message on Portfolio', #subject
            #     f'You have recieved a message from {name}: {msg}', #message
            #     ['ad747300@gmail.com'] # To 
            # )
    return render(request,'main/index.html',context)

