from django.shortcuts import render

# Create your views here.


def distance(request):
    return render(request, 'tools/distance.html')


def sub(request):
    return render(request, 'tools/sub.html')


def water(request):
    return render(request, 'tools/water.html')


def prn(request):
    return render(request, 'tools/print.html')


def roxar(request):
    return render(request, 'tools/roxar.html')
