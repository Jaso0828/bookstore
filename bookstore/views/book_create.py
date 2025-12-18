from ..models import Book
from django.views.generic import CreateView
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy ("book_list")