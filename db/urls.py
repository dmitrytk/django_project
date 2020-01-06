from django.urls import path

from .views import FieldView, DetailFieldView, edit_field, well_load

urlpatterns = [
    path('', FieldView.as_view(), name='fields'),
    path('<int:pk>', DetailFieldView.as_view(), name='field_detail'),
    path('<int:pk>/edit', edit_field, name='edit_field'),
    path('well_load/', well_load, name='well_load'),
]
