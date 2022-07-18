from django import forms


class FirstForm(forms.Form):
    name = forms.CharField(label="name", max_length=30, required=True)
    age = forms.IntegerField(label="age", required=True, min_value=0, max_value=100)
    level = forms.CharField(label="level", max_length=30, required=True)


class GetForm(forms.Form):
    numbers_1 = forms.IntegerField(label="Enter the value of the first leg", min_value=1, required=True)
    numbers_2 = forms.IntegerField(label="Enter the value of the second leg", min_value=1, required=True)


