from django.shortcuts import render, redirect
from .models import Project, Service, Message
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('it ran bro')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if message and email:
            new_msg = Message(name=name, email=email, message=message)
            new_msg.save()
            try:
                print('sending mail...')
                send_mail(
                    f"Message from {new_msg.name} on JossyTech Website",
                    new_msg.message,
                    new_msg.email,
                    ['mykelaloh@gmail.com'],
                )
                messages.success(request, 'Your message has been sent succesfully') 
            except Exception as e:
                err_msg = str(e)
                messages.error(request, f"An error occured while sending your message: {err_msg}")
        print(messages)
        return redirect('index')
    projects = Project.objects.all()
    services = Service.objects.all()
    context = {'projects': projects, 'services': services}
    print(context)
    return render(request, 'base.html', context=context)