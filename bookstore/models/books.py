from django.db import models
from .publishers import Publisher

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()   

    class Meta():
        ordering = ['-publication_date', 'title']
    
    def __str__(self):
        return f'{self.title} ({self.publication_date})'
    