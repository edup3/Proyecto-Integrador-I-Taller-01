from abc import ABC, abstractmethod


class BookSortStrategy(ABC):
    @abstractmethod
    def sort(self, queryset):
        pass
