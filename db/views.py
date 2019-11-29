from django.shortcuts import render
from .models import OilField
# Create your views here.


def db(request):
    fields = OilField.objects.all()
    return render(request, 'db/db.html', {'fields': fields})
