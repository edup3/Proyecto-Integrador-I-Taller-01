from .interfaces import BookSortStrategy
from .strategies import SortByRatingAsc, SortByRatingDesc, SortByGenre, SortBySubject
from .models import Book, BookDetails, Review
from django.shortcuts import get_object_or_404
from .interfaces import AbstractBookService
from django.utils import timezone
from datetime import date

class BookSorterService:
    STRATEGIES = {
        'asc': SortByRatingAsc(),
        'desc': SortByRatingDesc(),
        'genre': SortByGenre(),
        'subject': SortBySubject(),
    }

    @classmethod
    def sort_books(cls, queryset, sort_option):
        strategy = cls.STRATEGIES.get(sort_option)
        if strategy:
            return strategy.sort(queryset)
        return queryset

def cancel_reservation_automatic(request):
    expired_reservations = Book.objects.filter(
        reserved=True, reserved_date__lt=date.today())
    for book in expired_reservations:
        book.reserved = False
        book.reserved_date = None
        book.reserved_by = None
        book.save()


def check_rented(request):
    # Asegurarse de que la fecha es consciente de la zona horaria
    today = timezone.now().date()
    book_list = Book.objects.filter(real_availability__lt=today)
    for book in book_list:
        book.real_availability = None
        book.save()

class BookService(AbstractBookService):
    def handle_book_access(self, request):
        cancel_reservation_automatic(request)
        check_rented(request)

    def get_book(self, book_id):
        return get_object_or_404(Book, pk=book_id)

    def get_book_details(self, book):
        return BookDetails.objects.get(book=book)

    def get_reviews(self, book):
        return Review.objects.filter(book=book)