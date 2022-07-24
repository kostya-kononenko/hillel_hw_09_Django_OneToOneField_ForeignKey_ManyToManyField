from codebase.models import CRUD

from django import forms
from django.core.exceptions import ValidationError


class CRUDForm(forms.Form):
    name = forms.CharField(label="name", max_length=30, required=True)
    age = forms.IntegerField(label="age", required=True, min_value=0, max_value=100)
    level = forms.CharField(label="level", max_length=30, required=True)


class CRUDModelForm(forms.ModelForm):

    class Meta:
        model = CRUD
        fields = ["name", "age", "level"]

    def clean(self):
        cleaned_date = super().clean()
        name = cleaned_date.get("name")
        level = cleaned_date.get("level")
        if name == level:
            raise ValidationError("Name can`t be the same as Level ")
