from .interfaces import BookSortStrategy
from .strategies import SortByRatingAsc, SortByRatingDesc, SortByGenre, SortBySubject


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
