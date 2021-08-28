from django.db.models.expressions import OrderBy
from .models import Task
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request,name):
    return HttpResponse('bonjour à tous '+ name)  
def task_listing(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request,template_name='list2.html',context={'tasks':tasks})