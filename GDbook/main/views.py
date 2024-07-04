from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView
from .forms import BookForm
from .models import *


class BookCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Book
    # Класс на основе которого будет валидация полей
    form_class = BookForm
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'main/create.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = '/book'

class Delete(DeleteView):
    model = Book
    success_url = '/book'
    template_name ='main/delete.html'

def index(request):
    return render(request,'main/index.html')

def reviews(request):
    return render(request,'main/reviews.html')

def book(request):
    bok = Book.objects.all()
    return render(request,'main/book.html',{ 'bok':bok })

def sign(request):
    return render(request,'main/sign.html')



# def create(request):
#
#     return render(request,'main/create.html', )