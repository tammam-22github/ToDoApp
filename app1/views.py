from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
from .forms import TasksForm
from django import forms

# Create your views here.

def Home(request):
    return render(request,"app1/Home.html")

def DoList(request):
    tasks=Tasks.objects.all()
    form=TasksForm()
    if request.method=='POST':
        form=TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/dolist/")
    context={'tasks':tasks,'form':form}
    return render(request,"app1/DoList.html",context)

def update_task(request,pk):
    task=get_object_or_404(Tasks,id=pk)
    form=TasksForm(instance=task)
    if request.method=="POST":
        form=TasksForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/dolist/")
    context={'form':form}    
    return render(request,'app1/update_task.html',context)

def deletetask(request,pk):
    task=get_object_or_404(Tasks,id=pk)
    if  request.method=="POST":
        task.delete()
        return redirect("http://127.0.0.1:8000/dolist/")
    context={'task':task}
    return render(request,'app1/delete.html',context)

def createtask(request):
    create_task=TasksForm()
    if request.method=='POST':
        create_task=TasksForm(request.POST)
        if create_task.is_valid():
            create_task.save()
            return redirect("http://127.0.0.1:8000/dolist/")
        else:
            raise  forms.ValidationError("invalid inputs.\nplease try again.")
    else:
        create_task=TasksForm()
    return render(request,"app1/create.html",{'createform':create_task})        


def taskdetail(request,pk):
    task=get_object_or_404(Tasks,id=pk)
    return render(request,"app1/detail.html",{"task":task}) 