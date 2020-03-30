from django.shortcuts import render
from .forms import TextForm
from .models import ToDoText
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text_obj = ToDoText(text=form.cleaned_data["text"])
            text_obj.save()
        return HttpResponseRedirect('/todo')
    else:
        form = TextForm()
    return render(request, 'ToDoBox/index.html', {"form": form})
