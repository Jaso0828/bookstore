from ..models import Author
from django.views.generic import CreateView
from django.urls import reverse_lazy

class AuthorCreateView(CreateView):
    model = Author
    fields = "__all__"
    success_url = reverse_lazy ("author_list")