from django.urls import path

from triangle.views import crud_list_new, first_model_form, first_model_update_form, get_form


app_name = "triangle"
urlpatterns = [
    path('', crud_list_new, name='new-index'),
    path('getform/', get_form, name='get-form'),
    path('createform/', first_model_form, name='first-model-form'),
    path('first-model-form/<int:pk>/', first_model_update_form, name='first-model-update-form'),
]
