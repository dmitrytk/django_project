from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .models import Message


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        message = Message.objects.create(name=name, email=email, message=message)
        message.save()
        return redirect('home')
    else:
        return render(request, 'pages/index.html')


def distance(request):
    return render(request, 'pages/distance.html')


def sub(request):
    return render(request, 'pages/sub.html')


def water(request):
    return render(request, 'pages/water.html')


def prn(request):
    return render(request, 'pages/print.html')


def roxar(request):
    return render(request, 'pages/roxar.html')


def messages(request):
    messages = Message.objects.all()
    return render(request, 'pages/messages.html', {'messages': messages})


class DetailMessageView(DetailView):
    model = Message
    template_name = 'pages/message.html'
    context_object_name = 'message'


def message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message:
        message.unread = False
        message.save()
    return redirect(request, 'pages/message.html', {'message': message})
