from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import model_to_dict
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
    if request.method == 'POST':
        form = FieldUpdateForm(request.POST, instance=field)
        if form.is_valid():
            form.save()
            return redirect('fields')
    else:
        form = FieldUpdateForm(initial=model_to_dict(field))
    return render(request, 'db/update_field.html', {'form': form, 'field': field})
