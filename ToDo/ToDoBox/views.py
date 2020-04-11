import pandas as pd
import datetime
from plotly.offline import plot
from plotly.graph_objs import Bar
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
    all_todo_objects_today = ToDoText.objects.filter(data=datetime.date.today())
    return render(request, 'ToDoBox/index.html', {"form": form, "all_todo_objects_today": all_todo_objects_today})


def delete_todo(request, obj_id):
    deleted_item = ToDoText.objects.get(pk=obj_id)
    deleted_item.delete()
    return HttpResponseRedirect('/todo/')


def display(request):
    start_day = datetime.date.today() - datetime.timedelta(days=5)
    end_day = datetime.date.today()
    items = ToDoText.objects.filter(data__gte=start_day, data__lt=end_day).values()
    items = list(items)
    df = pd.DataFrame(items)
    x_data = df["data"]
    y_data = df.groupby('data').size()
    df_plot = plot([Bar(x=x_data, y=y_data)], output_type='div', include_plotlyjs=False,
                   show_link=False, link_text="")

    return render(request, 'TodoBox/display.html', {"items": items, "df_plot": df_plot})
