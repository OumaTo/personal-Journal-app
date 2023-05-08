from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from requests import request
from .models import journal
import datetime
from django.contrib import messages

def home(request):
    today = datetime.datetime.today()
    journals = journal.objects.all().values() 
    
    return render(request, 'journal.html', {'journals': journals, 'today' : today})

def add(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    if title and content:
        new_journal = journal(title = title, content = content)
        new_journal.save()
        return HttpResponseRedirect('/')
                
    # return render(request,'journal.html')
    return HttpResponseRedirect('/')



def update(request, id):
    journal_update = journal.objects.get(id=id)
    return render(request, 'update.html', {'journal_update': journal_update})


def delete(request, id):
  J = journal.objects.get(id=id)
  J.delete()
  return HttpResponseRedirect('/')

def updaterecord(request, id):
    title = request.POST.get('title')
    content = request.POST.get('content')
    J = journal.objects.get(id=id)
        
    J.title = title
    J.content = content
    J.save()
    
    return HttpResponseRedirect('/')