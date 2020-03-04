from django.urls import path

from .views import FieldView, DetailFieldView, WellView, DeleteFieldView, edit_field, load_wells, load_fields, \
    add_field, add_well

urlpatterns = [
    path('fields/', FieldView.as_view(), name='fields'),
    path('fields/<int:pk>', DetailFieldView.as_view(), name='field-detail'),
    path('fields/<int:pk>/edit', edit_field, name='field-edit'),
    path('fields/<int:pk>/delete', DeleteFieldView.as_view(), name='field-delete'),
    path('load_fields/', load_fields, name='fields-load'),
    path('add_field/', add_field, name='field-add'),
    path('wells/', WellView.as_view(), name='wells'),
    path('add_well/', add_well, name='well-add'),
    path('load_wells/', load_wells, name='wells-load'),
]
