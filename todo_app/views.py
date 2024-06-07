from django.shortcuts import redirect, render, get_object_or_404
from .models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    date = tasks[0].created_date
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'date': date
    }
    return render(request, 'home.html', context)

def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo = Task.objects.create(task=task)
        Todo.save()
        return redirect('home')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task_name = request.POST.get('task')
        task.task = task_name
        task.save()
        return redirect('home')
    context = {
        'task': task
    }
    return render(request, 'edit.html', context)

def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def pending_tasks(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
