from abc import ABC, abstractmethod


class BookSortStrategy(ABC):
    @abstractmethod
    def sort(self, queryset):
        pass

class AbstractBookService(ABC):
    @abstractmethod
    def handle_book_access(self, request): pass

    @abstractmethod
    def get_book(self, book_id): pass

    @abstractmethod
    def get_book_details(self, book): pass

    @abstractmethod
    def get_reviews(self, book): pass
