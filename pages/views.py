from django.shortcuts import render


def index(request):
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
