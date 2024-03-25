from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Review, Rating
from django.urls import reverse
import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .forms import LibroForm
from django.contrib.auth.decorators import login_required


def home(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, 'home.html', {'books': books, 'searchTerm': searchTerm})

@login_required
def rate_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        rating = request.POST.get('rating')
        
        if not rating:
            return HttpResponseBadRequest("No se ha proporcionado una calificación.")
        
        rating = int(rating)
        
        book = get_object_or_404(Book, id=book_id)
        user = request.user
        
        # Verificar si el usuario ya ha dejado un rating para este libro
        existing_rating = Rating.objects.filter(book=book, user=user).exists()
        if existing_rating:
            return HttpResponseBadRequest("Ya has dejado un rating para este libro.")
        
        # Crear el rating
        Rating.objects.create(book=book, user=user, value=rating)
        
        # Calcular el rating promedio del libro
        ratings = Rating.objects.filter(book=book)
        total_ratings = ratings.count()
        sum_ratings = sum(rating.value for rating in ratings)
        book.rating_average = sum_ratings / total_ratings
        book.save()
        
    return redirect('home')
 

def submit_review(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        review_text = request.POST.get('reviewText')
        book = Book.objects.get(id=book_id)
        Review.objects.create(book=book, text=review_text)
        # Redirige a la página de descripción del libro con el ancla del comentario
        return HttpResponseRedirect(reverse('book_details', args=(book_id,)) + '#reviews')
    else:
        return redirect('home')

def about(request):
    return render(request, 'about.html')

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'book_description.html', {'book': book, 'reviews': reviews})


"""def book_description(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_description.html', {'book': book})"""

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
    return HttpResponseRedirect(reverse('book_details', args=(book_id,)))

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
    return HttpResponseRedirect(reverse('book_details', args=(book_id,)))



def change_real_availability(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if book.real_available:
        book.real_available = False
        book.real_availability = datetime.date.today() + datetime.timedelta(days=14)
    else:
        book.real_available = True
        book.real_availability = None 
        
    book.save()
    
    return HttpResponseRedirect(reverse('book_details', args=(book_id,)))

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
    
    # Redirigir a la página de descripción del libro actualizado
    return HttpResponseRedirect(reverse('book_details', args=(book_id,)))

def add_book(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir a una página de éxito o realizar otra acción
    else:
        form = LibroForm()
    
    return render(request, 'form.html', {'form': form})
    

    