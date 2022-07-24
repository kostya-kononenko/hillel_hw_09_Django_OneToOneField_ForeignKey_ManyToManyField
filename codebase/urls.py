from codebase.views import crud_list, form, model_form, model_update_form

from django.urls import path


app_name = "codebase"
urlpatterns = [
    path('', crud_list, name='index'),
    path('<int:age>/', crud_list, name='crud-filter'),
    path('form/', form, name='form'),
    path('model-form/', model_form, name='model-form'),
    path('model-form/<int:pk>/', model_update_form, name='model-update-form'),
]
