from ..models.books import Book

from django.views.generic import ListView

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'


    