import datetime
from django.shortcuts import render
from .forms import TextForm
from .models import ToDoText
from django.db.models import Count
from django.http import JsonResponse
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
    all_todo_objects_today = ToDoText.objects.filter(date=datetime.date.today())
    return render(request, 'ToDoBox/index.html', {"form": form, "all_todo_objects_today": all_todo_objects_today})


def delete_todo(request, obj_id):
    deleted_item = ToDoText.objects.get(pk=obj_id)
    deleted_item.delete()
    return HttpResponseRedirect('/todo/')


def display(request):
    return render(request, 'ToDoBox/display.html')


def activities_chart(request):
    labels = []
    data = []
    start_day = datetime.date.today() - datetime.timedelta(days=8)
    items = ToDoText.objects.values('date').annotate(number_of_activities=Count('date')).filter(date__gt=start_day)
    for number in range(7, -1, -1):
        temp_today = datetime.date.today() - datetime.timedelta(days=number)
        labels.append(temp_today)
    for date in labels:
        for item in items:
            if item["date"] == date:
                data.append(item['number_of_activities'])
                break
            else:
                if item == list(items)[-1]:
                    data.append(0)
                continue
    return JsonResponse(data={"labels": labels, "data": data})
