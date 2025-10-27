# 📚 Book Review Management System

A full-featured Django web application for managing books, authors, and user reviews with a customized admin panel and beautiful frontend interface.

![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### Admin Panel
- ✨ **Custom Admin Interface** with branding and customizations
- 🔍 **Advanced Filtering** by category, author, and publication year
- 🔎 **Search Functionality** by title and ISBN
- ✏️ **Inline Review Editing** directly within book management
- 📊 **Field Grouping** with organized fieldsets
- ⚡ **Custom Actions** for bulk operations (e.g., Mark as Top Rated)
- 📝 **List Editable Fields** for quick updates
- 🔒 **Read-only Fields** for data integrity

### Frontend
- 🎨 **Modern UI** with gradient design and Bootstrap 5
- 📖 **Book Browsing** with grid layout
- 🔍 **Search & Filter** by title and category
- 📄 **Detailed Book Pages** with author information
- ⭐ **Review System** with star ratings
- ➕ **Add Books** through user-friendly forms
- 📱 **Responsive Design** for all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/bookreview-project.git
cd bookreview-project
```

2. **Create and activate virtual environment**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

6. **Start the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Frontend: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
bookreview_project/
├── bookreview/                 # Main application
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   └── bookreview/
│   │       ├── base.html
│   │       ├── book_list.html
│   │       ├── book_detail.html
│   │       └── book_form.html
│   ├── __init__.py
│   ├── admin.py               # Admin customizations
│   ├── apps.py
│   ├── models.py              # Data models
│   ├── urls.py                # App URL configuration
│   └── views.py               # View functions
├── bookreview_project/         # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🗃️ Database Models

### Author
- `name` - Author's full name
- `bio` - Biography (optional)
- `birth_date` - Date of birth (optional)

### Book
- `title` - Book title
- `author` - Foreign key to Author
- `isbn` - 13-digit ISBN (unique)
- `published_date` - Publication date
- `category` - Fiction, Non-fiction, Sci-fi, Fantasy, or Other
- `rating` - Average rating (0-5)

### Review
- `book` - Foreign key to Book
- `reviewer_name` - Name of the reviewer
- `rating` - Rating (1-5 stars)
- `comment` - Review text
- `created_at` - Timestamp

## 🎯 Usage

### Admin Panel

1. **Access Admin Panel**
   - Navigate to http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

2. **Manage Authors**
   - Add new authors with bio and birth date
   - View book count for each author

3. **Manage Books**
   - Add books with complete details
   - Use inline review editor
   - Apply bulk actions (e.g., Mark as Top Rated)
   - Filter by category, author, or publication year
   - Search by title or ISBN

4. **Manage Reviews**
   - View all reviews
   - Filter by rating and date
   - Rating becomes read-only after creation

### Frontend

1. **Browse Books**
   - View all books at http://127.0.0.1:8000/books/
   - Search by title
   - Filter by category

2. **View Book Details**
   - Click on any book to see full details
   - Read all reviews
   - Add your own review

3. **Add New Books**
   - Click "Add Book" in navigation
   - Fill in required information
   - Submit to add to collection

## 🛠️ Technologies Used

- **Backend:** Django 5.x
- **Frontend:** HTML5, CSS3, Bootstrap 5.3
- **Database:** SQLite3
- **Icons:** Bootstrap Icons
- **Python:** 3.8+

## 📋 Admin Customizations

### Custom List Displays
- Books: title, author, category, rating, published date, review count
- Authors: name, birth date, book count
- Reviews: book, reviewer name, rating, created date

### Custom Filters
- Category filter
- Author filter
- Published this year filter

### Custom Actions
- Mark selected books as Top Rated (5.0 stars)

### Fieldsets
Books are organized into logical sections:
- Basic Info (title, author, category)
- Publication Details (ISBN, published date)
- Rating

## 🎨 Screenshots

### Homepage
Beautiful gradient design with book cards displaying key information.

### Book Detail Page
Comprehensive book information with author details and user reviews.

### Admin Panel
Customized admin interface with filters, search, and inline editing.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Bootstrap Icons
- All contributors

## 📧 Contact

For questions or feedback, please open an issue on GitHub or contact me at your.email@example.com

---

## 🚀 Future Enhancements

- [ ] User authentication for reviews
- [ ] Book cover image uploads
- [ ] Advanced search with multiple filters
- [ ] Export books to CSV/PDF
- [ ] API endpoints for mobile apps
- [ ] Email notifications for new reviews
- [ ] Book recommendations based on ratings

## 💡 Tips

- Use the admin panel for quick data management
- The custom "Published This Year" filter helps find recent books
- Use the bulk action to quickly mark multiple books as top rated
- Reviews are automatically timestamped
- Search works with partial matches

## 🔐 Security Notes

- Always change the default SECRET_KEY in production
- Set DEBUG=False in production
- Use environment variables for sensitive data
- Implement proper user authentication
- Regular security updates

---

**Built with ❤️ using Django**
