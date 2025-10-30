from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book, Review
from .serializers import (
    AuthorSerializer, 
    BookSerializer, 
    BookListSerializer, 
    ReviewSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Authors
    
    list: Get all authors
    retrieve: Get a single author by ID
    create: Create a new author
    update: Update an author
    partial_update: Partially update an author
    destroy: Delete an author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'bio']
    ordering_fields = ['name', 'birth_date']
    ordering = ['name']
    
    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        """Get all books by this author"""
        author = self.get_object()
        books = author.books.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Books
    
    list: Get all books
    retrieve: Get a single book by ID
    create: Create a new book
    update: Update a book
    partial_update: Partially update a book
    destroy: Delete a book
    """
    queryset = Book.objects.all().select_related('author')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'isbn']
    ordering_fields = ['title', 'published_date', 'rating']
    ordering = ['-published_date']
    
    def get_serializer_class(self):
        """Use different serializers for list and detail views"""
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Get all reviews for this book"""
        book = self.get_object()
        reviews = book.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        """Add a review to this book"""
        book = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        """Get top rated books (rating >= 4.0)"""
        books = self.queryset.filter(rating__gte=4.0).order_by('-rating')
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get books grouped by category"""
        categories = {}
        for choice in Book.CATEGORY_CHOICES:
            category = choice[0]
            books = self.queryset.filter(category=category)
            categories[category] = BookListSerializer(books, many=True).data
        return Response(categories)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Reviews
    
    list: Get all reviews
    retrieve: Get a single review by ID
    create: Create a new review
    update: Update a review
    partial_update: Partially update a review
    destroy: Delete a review
    """
    queryset = Review.objects.all().select_related('book', 'book__author')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['book', 'rating']
    ordering_fields = ['created_at', 'rating']
    ordering = ['-created_at']
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent reviews (last 10)"""
        recent_reviews = self.queryset[:10]
        serializer = self.serializer_class(recent_reviews, many=True)
        return Response(serializer.data)