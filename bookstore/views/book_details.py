from ..models.books import Book

from django.views.generic import  DetailView


class BookDetailView(DetailView):
    model = Book