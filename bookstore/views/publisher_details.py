from django.views.generic import DetailView
from ..models.publishers import Publisher


class PublisherDetailView(DetailView):
    model = Publisher