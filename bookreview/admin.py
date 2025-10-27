from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from .models import Author, Book, Review


# Custom Admin Site Branding
admin.site.site_header = "Book Review Management Admin"
admin.site.site_title = "Book Review Portal"
admin.site.index_title = "Manage Books, Authors, and Reviews"


# Custom List Filter - Books published in the last year
class PublishedThisYearFilter(admin.SimpleListFilter):
    title = 'published this year'
    parameter_name = 'published_year'
    
    def lookups(self, request, model_admin):
        return (
            ('yes', 'Published this year'),
            ('last_year', 'Published last year'),
        )
    
    def queryset(self, request, queryset):
        now = timezone.now()
        if self.value() == 'yes':
            return queryset.filter(
                published_date__year=now.year
            )
        if self.value() == 'last_year':
            return queryset.filter(
                published_date__year=now.year - 1
            )


# Inline Review Editor (shows reviews inside Book admin)
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # Number of empty forms to display
    fields = ('reviewer_name', 'rating', 'comment', 'created_at')
    readonly_fields = ('created_at',)


# Author Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'book_count')
    search_fields = ('name', 'bio')
    list_filter = ('birth_date',)
    
    # Custom method to show number of books
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'


# Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display columns in list view
    list_display = ('title', 'author', 'category', 'rating', 'published_date', 'review_count')
    
    # Filters on right sidebar
    list_filter = ('category', 'author', PublishedThisYearFilter)
    
    # Search functionality
    search_fields = ('title', 'isbn')
    
    # Allow editing rating directly in list view
    list_editable = ('rating',)
    
    # Inline reviews
    inlines = [ReviewInline]
    
    # Field grouping (fieldsets)
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'author', 'category')
        }),
        ('Publication Details', {
            'fields': ('isbn', 'published_date')
        }),
        ('Rating', {
            'fields': ('rating',)
        }),
    )
    
    # Custom actions
    actions = ['make_top_rated']
    
    @admin.action(description='Mark selected books as Top Rated (5.0)')
    def make_top_rated(self, request, queryset):
        updated = queryset.update(rating=5.0)
        self.message_user(request, f'{updated} book(s) marked as Top Rated (5.0 stars).')
    
    # Custom method to show review count
    def review_count(self, obj):
        return obj.reviews.count()
    review_count.short_description = 'Reviews'


# Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('reviewer_name', 'book__title', 'comment')
    readonly_fields = ('created_at',)
    
    # Make rating readonly after creation
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('rating',)
        return self.readonly_fields