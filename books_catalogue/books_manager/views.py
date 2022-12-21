from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request)->render:
    books=Book.objects.all()
    template_='index.html'
    context={
        'books':books,
    }
    return render(request,template_,context=context)

