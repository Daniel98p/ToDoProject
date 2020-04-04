from django.shortcuts import render
from .forms import TextForm
from .models import ToDoText
from django.http import HttpResponseRedirect
from datetime import date


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text_obj = ToDoText(text=form.cleaned_data["text"])
            text_obj.save()
        return HttpResponseRedirect('/todo')
    else:
        form = TextForm()
    all_todo_objects_today = ToDoText.objects.filter(data=date.today())
    return render(request, 'ToDoBox/index.html', {"form": form, "all_todo_objects_today": all_todo_objects_today})


def delete_todo(request, obj_id):
    deleted_item = ToDoText.objects.get(pk=obj_id)
    deleted_item.delete()
    return HttpResponseRedirect('/todo/')
