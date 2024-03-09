from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import Book
from django.urls import reverse
import datetime

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


def adminrent(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    return render(request, 'adminrent.html', {'book': book})




def change_availability(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    # Cambiar el estado de disponibilidad
    if book.available:
        book.available = False
        book.availability = datetime.date.today() + datetime.timedelta(days=31)  # Establecer la disponibilidad en 31 días desde hoy
    else:
        book.available = True
        book.availability = None
    
    book.save()
    
    # Redirigir a la página de descripción del libro actualizado
    return HttpResponseRedirect(reverse('book_description', args=(book_id,)))

def reserve_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    # Cambiar el estado de reserva
    if book.reserved:
        book.reserved = False
        book.reserved_date = None
    else:
        book.reserved = True
        book.reserved_date = datetime.date.today() + datetime.timedelta(days=7)  # Establecer la fecha de reserva en 7 días desde hoy
    
    book.save()
    
    # Redirigir a la página de descripción del libro actualizado
    return HttpResponseRedirect(reverse('book_description', args=(book_id,)))

def change_real_availability(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if book.real_available:
        book.real_available = False
        book.real_availability = datetime.date.today() + datetime.timedelta(days=14)
    else:
        book.real_available = True
        book.real_availability = None 
        
    book.save()
    
    return HttpResponseRedirect(reverse('book_description', args=(book_id,)))

def verify_availability(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if book.real_available and not book.reserved:
        book.available = True
        book.availability = None
    elif book.real_available and book.reserved:
        book.available = False
        book.availability = book.reserved_date + datetime.timedelta(days=14)
    else:
        book.available = False
        book.availability = book.real_availability
        
    book.save()
    
    
    
    