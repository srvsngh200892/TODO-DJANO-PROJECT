from task_manager.forms import *
from task_manager.taskform import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from task_manager.models import task

 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
def task_added(request):
    return render_to_response(
    'taskadded.html',
    )    
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    task_data= task.objects.filter(user_name_id=request.user.id)
    task_data_public= task.objects.filter(visibilty=2)
    
    return render_to_response(
    'home.html',
    { 'user': request.user ,'task_data':task_data,'task_data_public':task_data_public}
    )

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(
            title=form.cleaned_data['title'],
            created_date=form.cleaned_data['created_date'],
            priority=form.cleaned_data['email'],
            visibilty=form.cleaned_data['visibilty'],
            status=form.cleaned_data['status']
            )
            return HttpResponseRedirect('/home/taskadded/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'addtask.html',
    variables,
    )