from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Book

def home(request):

    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, 'home.html', {'books': books, 'searchTerm': searchTerm})

def about(request):
    return render(request, 'about.html')

def book_description(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_description.html', {'book': book})