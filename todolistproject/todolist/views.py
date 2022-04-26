from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


# Create your views here.
class IndexListview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'




class updateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

def __success_url(self):
    return reverse_lazy('cbvdetail',{'pk'},kwargs=Task.object.id)



def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task',)
        priority=request.POST.get('priority',)
        date=request.POST.get('date',)
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"index.html",{'task':task1})
def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
    return render(request,'delete.html')
def update(request,taskid):
    task=Task.objects.get(id=taskid)
    form=TaskForm(request.POST or None,instances=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})