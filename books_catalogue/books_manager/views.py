from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request)->render:
    books={
    'Harry Potter':'J W Rowling',
    'War and Peace':'Leo Tolstoi',
    'Swim in a Pond in the Rain':'George Saunders',
    ' Living with a Dead Language':'Pat Pattison'
}
    sorted_books=dict(sorted(books.items()))
    template_='index.html'
    context={
        'books':sorted_books,
    }
    return render(request,template_,context=context)

