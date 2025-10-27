from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg
from .models import Book, Author, Review


def book_list(request):
    """Display all books"""
    books = Book.objects.all().select_related('author')
    
    # Filter by category if provided
    category = request.GET.get('category')
    if category:
        books = books.filter(category=category)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        books = books.filter(title__icontains=search_query)
    
    context = {
        'books': books,
        'total_books': books.count(),
        'categories': Book.CATEGORY_CHOICES,
        'selected_category': category,
        'search_query': search_query
    }
    return render(request, 'bookreview/book_list.html', context)


def book_detail(request, pk):
    """Display book details with reviews"""
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    
    # Handle review submission
    if request.method == 'POST':
        reviewer_name = request.POST.get('reviewer_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if reviewer_name and rating and comment:
            Review.objects.create(
                book=book,
                reviewer_name=reviewer_name,
                rating=int(rating),
                comment=comment
            )
            messages.success(request, 'Your review has been added successfully!')
            return redirect('book_detail', pk=pk)
        else:
            messages.error(request, 'Please fill in all fields.')
    
    # Calculate average rating
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating is None:
        avg_rating = 0
    
    context = {
        'book': book,
        'reviews': reviews,
        'average_rating': round(avg_rating, 1)
    }
    return render(request, 'bookreview/book_detail.html', context)


def book_create(request):
    """Create a new book"""
    authors = Author.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')
        category = request.POST.get('category')
        rating = request.POST.get('rating', 0)
        
        if title and author_id and isbn and published_date and category:
            try:
                author = Author.objects.get(pk=author_id)
                Book.objects.create(
                    title=title,
                    author=author,
                    isbn=isbn,
                    published_date=published_date,
                    category=category,
                    rating=float(rating)
                )
                messages.success(request, f'Book "{title}" added successfully!')
                return redirect('book_list')
            except Author.DoesNotExist:
                messages.error(request, 'Selected author does not exist.')
            except Exception as e:
                messages.error(request, f'Error adding book: {str(e)}')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    context = {
        'authors': authors,
        'categories': Book.CATEGORY_CHOICES
    }
    return render(request, 'bookreview/book_form.html', context)