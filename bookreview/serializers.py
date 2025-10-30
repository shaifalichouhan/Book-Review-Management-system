from rest_framework import serializers
from .models import Author, Book, Review


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model"""
    book_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_date', 'book_count']
    
    def get_book_count(self, obj):
        return obj.books.count()


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    
    class Meta:
        model = Review
        fields = ['id', 'book', 'reviewer_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model"""
    author_name = serializers.CharField(source='author.name', read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_name', 'isbn', 
            'published_date', 'category', 'rating', 
            'reviews', 'review_count', 'average_rating'
        ]
    
    def get_review_count(self, obj):
        return obj.reviews.count()
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return round(sum(r.rating for r in reviews) / len(reviews), 1)
        return 0


class BookListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for book list (without reviews)"""
    author_name = serializers.CharField(source='author.name', read_only=True)
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_name', 
            'isbn', 'published_date', 'category', 
            'rating', 'review_count'
        ]
    
    def get_review_count(self, obj):
        return obj.reviews.count()