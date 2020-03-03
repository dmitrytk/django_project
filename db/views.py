from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

from .forms import FieldUpdateForm, FieldCreateForm
from .models import OilField, Well
from .load import upload_wells, upload_fields


class FieldView(ListView):
    model = OilField
    template_name = 'db/fields.html'
    context_object_name = 'fields'


class WellView(ListView):
    model = Well
    template_name = 'db/wells.html'
    context_object_name = 'wells'


class DetailFieldView(DetailView):
    model = OilField
    template_name = 'db/field_detail.html'
    context_object_name = 'field'


def edit_field(request, pk):
    field = get_object_or_404(OilField, pk=pk)
    if request.method == 'POST':
        form = FieldUpdateForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect('fields')
    else:
        form = FieldUpdateForm(instance=field)
    return render(request, 'db/update_field.html', {'form': form, 'field': field})


def load_wells(request):
    if request.method == 'POST':
        upload_wells(request.POST.get('well-data'))
        return redirect('wells')
    return render(request, 'db/load_wells.html')


def load_fields(request):
    if request.method == 'POST':
        # upload_fields(request.POST.get('field-data'))
        print(request.POST.get('option-1'))
    return render(request, 'db/load_fields.html')


def add_field(request):
    if request.method == 'POST':
        form = FieldCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fields')
    else:
        form = FieldUpdateForm()
    return render(request, 'db/add_field.html', {'form': form})
