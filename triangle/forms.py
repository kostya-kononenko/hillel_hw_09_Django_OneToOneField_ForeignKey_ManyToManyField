from django import forms


class GetForm(forms.Form):
    numbers_1 = forms.IntegerField(label="Enter the value of the first leg", min_value=1, required=True)
    numbers_2 = forms.IntegerField(label="Enter the value of the second leg", min_value=1, required=True)
