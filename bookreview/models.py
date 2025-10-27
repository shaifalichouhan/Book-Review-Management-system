from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# Book Model
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-fiction', 'Non-fiction'),
        ('Sci-fi', 'Sci-fi'),
        ('Fantasy', 'Fantasy'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']


# Review Model
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title} ({self.rating}★)"
    
    class Meta:
        ordering = ['-created_at']