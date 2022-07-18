from django.urls import path

from triangle.views import form, get_form

urlpatterns = [
    path('form/', form, name='form'),
    path('getform/', get_form, name='getform'),
]
