from django.urls import path

from .views import FieldView, DetailFieldView

urlpatterns = [
    path('', FieldView.as_view(), name='fields'),
    path('<int:pk>', DetailFieldView.as_view(), name='field_detail'),
]
