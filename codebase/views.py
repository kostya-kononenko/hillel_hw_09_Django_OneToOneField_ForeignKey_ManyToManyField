from codebase.forms import CRUDForm, CRUDModelForm
from codebase.models import CRUD

from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    return render(request, "codebase/index.html", {})


def crud_list(request, age=None):
    if age:
        objects = CRUD.objects.filter(age=age)
    else:
        objects = CRUD.objects.all()
    return render(
        request,
        "codebase/list.html",
        {
            "objects": objects,
            "age": age,
        }
    )


def form(request):
    if request.method == 'POST':
        crud_form = CRUDForm(request.POST)
        if crud_form.is_valid():
            CRUD.objects.create(
                name=crud_form.cleaned_data["name"],
                age=crud_form.cleaned_data["age"],
                level=crud_form.cleaned_data["level"],
            )
            return redirect("codebase:index")
    else:
        crud_form = CRUDForm(initial={"age": 10})
    return render(
        request,
        "codebase/codebase_form.html",
        {
            "crud_form": crud_form
        }
    )


def model_form(request):
    if request.method == 'POST':
        crud_form = CRUDModelForm(request.POST)
        if crud_form.is_valid():
            crud_form.save()
            return redirect("codebase:index")
    else:
        crud_form = CRUDModelForm(initial={"age": 10})
    return render(
        request,
        "codebase/codebase_model_form.html",
        {
            "crud_form": crud_form
        }
    )


def model_update_form(request, pk):
    obj = get_object_or_404(CRUD, pk=pk)
    if request.method == 'POST':
        crud_form = CRUDModelForm(request.POST, instance=obj)
        if crud_form.is_valid():
            crud_form.save()
            return redirect("codebase:index")

    else:
        crud_form = CRUDModelForm(instance=obj)
    return render(
        request,
        "codebase/codebase_update_form.html",
        {
            "crud_form": crud_form,
            "obj": obj,
        }
    )
