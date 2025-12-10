from django.urls import path
from .views import (PublisherListView, 
                    PublisherDetailView,
                    BookDetailView, 
                    BookListView)


urlpatterns = [
    path('publishers/', PublisherListView.as_view()),
    path('publishers/<int:pk>', PublisherDetailView.as_view()),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>', BookDetailView.as_view())
]