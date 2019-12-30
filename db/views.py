from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
from .forms import FieldUpdateForm

from .models import OilField


class FieldView(ListView):
    model = OilField
    template_name = 'db/fields.html'
    context_object_name = 'fields'


class DetailFieldView(DetailView):
    model = OilField
    template_name = 'db/field_detail.html'
    context_object_name = 'field'


def edit_field(request, pk):
    field = get_object_or_404(OilField, pk=pk)
    form = FieldUpdateForm()
    if request.method == 'POST':
        form = FieldUpdateForm(request.POST)
        if form.is_valid():
            field.name = form.cleaned_data['name']
            field.type = form.cleaned_data['type']
            field.location = form.cleaned_data['location']
            field.owner = form.cleaned_data['owner']
            field.description = form.cleaned_data['description']
            field.obzor_img = form.cleaned_data['obzor_img']
            field.save()
            return redirect('fields')
    else:
        form = FieldUpdateForm()
    return render(request, 'db/update_field.html', {'form': form, 'field': field})
