from django.shortcuts import get_object_or_404, redirect, render

from triangle.forms import FirstModelForm, GetForm
from triangle.models import FirstForms


def get_form(request):
    calc = None
    if "submit" in request.GET:
        _get_form = GetForm(request.GET)
        if _get_form.is_valid():
            numbers_1 = _get_form.cleaned_data["numbers_1"]
            numbers_2 = _get_form.cleaned_data["numbers_2"]

            calc = ((numbers_1 ** 2) + (numbers_2 ** 2)) ** .5
    else:
        _get_form = GetForm(initial={"numbers_1": 0, "numbers_2": 0})
    return render(
        request,
        "triangle/get_forms.html",
        {
            "get_form": _get_form,
            "calc": calc,
        }
    )


def new_index(request):
    return render(request, "triangle/index.html", {})


def crud_list_new(request):
    objects = FirstForms.objects.all()
    return render(
        request,
        "triangle/list.html",
        {
            "objects": objects,
        }
    )


def first_model_form(request):
    if request.method == 'POST':
        first_form = FirstModelForm(request.POST)
        if first_form.is_valid():
            first_form.save()
            return redirect("index")
    else:
        first_form = FirstModelForm()
    return render(
        request,
        "triangle/codebase_model_form.html",
        {
            "first_form": first_form
        }
    )


def first_model_update_form(request, pk):
    obj = get_object_or_404(FirstForms, pk=pk)
    if request.method == 'POST':
        first_form = FirstModelForm(request.POST, instance=obj)
        if first_form.is_valid():
            first_form.save()
            return redirect("index")

    else:
        first_form = FirstModelForm(instance=obj)
    return render(
        request,
        "triangle/codebase_update_form.html",
        {
            "first_form": first_form,
            "obj": obj,
        }
    )
