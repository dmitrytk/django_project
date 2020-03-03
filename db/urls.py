from django.urls import path

from .views import FieldView, DetailFieldView, WellView, edit_field, load_wells, load_fields, add_field

urlpatterns = [
    path('fields/', FieldView.as_view(), name='fields'),
    path('wells/', WellView.as_view(), name='wells'),
    path('<int:pk>', DetailFieldView.as_view(), name='field_detail'),
    path('<int:pk>/edit', edit_field, name='edit_field'),
    path('load_wells/', load_wells, name='load-wells'),
    path('load_fields/', load_fields, name='load-fields'),
    path('add_field/', add_field, name='add-field'),
]
