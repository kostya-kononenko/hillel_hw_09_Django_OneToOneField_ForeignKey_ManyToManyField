from django.shortcuts import render, redirect
from triangle.forms import FirstForm, GetForm


def index(request):
    return render(request, "triangle/index.html", {})


def form(request):
    if request.method == 'POST':
        first_form = FirstForm(request.POST)
        if first_form.is_valid():
            print(first_form.cleaned_data)
            return redirect("index")
    else:
        first_form = FirstForm(initial={"age" : 10})
    return render(
        request,
        "triangle/codebase_forms.html",
        {
            "first_form": first_form,
        }
    )


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

