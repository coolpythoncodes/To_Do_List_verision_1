from datetime import date
import calendar

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import ListForm
from .models import List
# Create your views here.

def home(request):
    
    my_date = date.today()
    day=calendar.day_name[my_date.weekday()]
    if request.method == "POST":
        form =ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_task = List.objects.order_by("-completed")
            messages.success(request,"New task has been added")
            return render(request,"home.html",{"act":all_task,"day":day})
    else:
        all_task = List.objects.order_by("-completed")
        return render(request,"home.html",{"act":all_task,"day":day})



def about(request):
    return render(request,"about.html",{})

def remove(request,list_id):
    task = List.objects.get(pk=list_id)
    task.delete()
    return redirect("home")

def clear(request):
    task = List.objects.all().delete()
    
    return redirect("home")

def check(request,list_id):
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect("home")

def uncheck(request,list_id):
    task = List.objects.get(pk=list_id)
    task.completed = False
    task.save()
    return redirect("home")
