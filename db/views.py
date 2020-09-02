from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FieldUpdateForm, FieldCreateForm, WellCreateForm
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


class DeleteFieldView(LoginRequiredMixin,DeleteView):
    model = OilField
    template_name = 'db/field_delete.html'
    success_url = reverse_lazy('fields')

@login_required
def edit_field(request, pk):
    field = get_object_or_404(OilField, pk=pk)
    if request.method == 'POST':
        form = FieldUpdateForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect('fields')
    else:
        form = FieldUpdateForm(instance=field)
    return render(request, 'db/field_edit.html', {'form': form, 'field': field})

# LOAD DATA
@login_required
def load_wells(request):
    if request.method == 'POST':
        upload_wells(request.POST.get('well-data'))
        return redirect('wells')
    return render(request, 'db/wells_load.html')

@login_required
def load_fields(request):
    if request.method == 'POST':
        upload_fields(request.POST.get('field-data'))
        return redirect('fields')
    return render(request, 'db/fields_load.html')

# ADD DATA
@login_required
def add_field(request):
    if request.method == 'POST':
        form = FieldCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fields')
    else:
        form = FieldCreateForm()
    return render(request, 'db/field_add.html', {'form': form})

@login_required
def add_well(request):
    if request.method == 'POST':
        form = WellCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wells')
    else:
        form = WellCreateForm()
    return render(request, 'db/well_add.html', {'form': form})
