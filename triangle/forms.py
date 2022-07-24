from django import forms

from triangle.models import FirstForms


class GetForm(forms.Form):
    numbers_1 = forms.IntegerField(label="Enter the value of the first leg", min_value=1, required=True)
    numbers_2 = forms.IntegerField(label="Enter the value of the second leg", min_value=1, required=True)


class FirstModelForm(forms.ModelForm):

    class Meta:
        model = FirstForms
        fields = ["first_name", "last_name", "email_field"]
