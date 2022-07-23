from django.urls import path

from triangle.views import get_form

urlpatterns = [
    path('getform/', get_form, name='get-form'),
]
