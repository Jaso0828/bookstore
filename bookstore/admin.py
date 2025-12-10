from django.contrib import admin

from .models.authors import Author
from .models.books import Book
from .models.publishers import Publisher

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)