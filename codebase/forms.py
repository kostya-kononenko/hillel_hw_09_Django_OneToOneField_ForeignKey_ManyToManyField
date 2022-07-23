from django import forms


class CRUDForm(forms.Form):
    name = forms.CharField(label="name", max_length=30, required=True)
    age = forms.IntegerField(label="age", required=True, min_value=0, max_value=100)
    level = forms.CharField(label="level", max_length=30, required=True)
