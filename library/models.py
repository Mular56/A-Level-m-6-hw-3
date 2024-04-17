from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books_written')
    is_available = models.BooleanField(default=True)
    borrower = models.CharField(max_length=100, blank=True, null=True)
    borrowed_date = models.DateField(blank=True, null=True) 
    
    def borrow(self, borrower_name):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrower_name = borrower_name
            self.save()
            return True
        return False
    
    def return_book(self):     # повернення позиченої книги
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrower_name = None
            self.save()
            return True
        return False
    
    def __str__(self):
        authors_names = ', '.join(str(author) for author in self.authors.all())
        return f"{self.title} by {authors_names}"
