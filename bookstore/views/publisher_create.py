from ..models import Publisher
from django.views.generic import CreateView
from django.urls import reverse_lazy

class PublisherCreateView(CreateView):
    model = Publisher
    fields = "__all__"
    success_url = reverse_lazy ("author_list")