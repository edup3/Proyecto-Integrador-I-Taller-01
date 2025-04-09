from .interfaces import BookSortStrategy


class SortByRatingAsc(BookSortStrategy):
    def sort(self, queryset):
        return queryset.order_by('rating_average')


class SortByRatingDesc(BookSortStrategy):
    def sort(self, queryset):
        return queryset.order_by('-rating_average')


class SortByGenre(BookSortStrategy):
    def sort(self, queryset):
        return queryset.order_by('bookdetails__genre')


class SortBySubject(BookSortStrategy):
    def sort(self, queryset):
        return queryset.order_by('bookdetails__subject')
