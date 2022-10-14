import re
from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    todo = ToDo.objects.all()
    return render(request, 'index.html', {'todo':todo})

def create(request):
    if request.method == 'POST':
        todo = ToDo()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')

def delete_letter(request, id):
    todo = ToDo.objects.get(id = id)
    deleted_todo = Delete()
    deleted_todo.deleted_title = todo.title
    deleted_todo.deleted_description = todo.description
    deleted_todo.save()
    todo.delete()
    return HttpResponseRedirect('/')

def cart(request):
    deleted_todo = Delete.objects.all()
    return render(request, 'page3.html', {'deleted_todo': deleted_todo})

def edit_letter(request, id):
    todo = ToDo.objects.get(id = id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render (request, 'page2.html', {'todo': todo})



def favourites(request, id):
    todo = ToDo.objects.get(id=id)
    favourite = Favourites()
    favourite.favourite_title= todo.title
    favourite.favourite_description = todo.description
    favourite.favourite_sent_at = todo.sent_at
    favourite.save()
    return HttpResponseRedirect('/')

def favourites_page(request):
    favourite = Favourites.objects.all()
    return render(request, 'favourites.html', {'favourite': favourite})