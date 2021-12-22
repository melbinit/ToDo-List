import contextlib
from typing import ContextManager
from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Task

# Create your views here.

def home(request):
    context = { 'success':False}
    if request.method== "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        ins = Task(tasktitle=title, taskdesc=desc)
        ins.save()
        context = {'success' :True}
    return render(request, "index.html",context)


def tasks(request):
    alltasks = Task.objects.all()
    context = { 'tasks' : alltasks}
    return render(request, "tasks.html",context)
