# 📚 Books & Authors — Django MTV Assignment

A full-stack Django web application that manages books and authors using a **Many-to-Many relationship**.

---

## 🎯 What This App Does

- Add books and authors to a database
- View all books / all authors in a table
- View details of a single book — including all its authors
- View details of a single author — including all their books
- Link authors to books (and books to authors) via a dropdown
- ⭐ **BONUS**: Dropdown only shows unlinked authors/books

---

## 🗂️ Project Structure

```
book_authours_temps/
├── my_app/
│   ├── models.py          ← Book & Author models
│   ├── views.py           ← All page logic
│   ├── urls.py            ← All routes
│   └── templates/
│       └── my_app/
│           ├── books.html          ← Book list + add form
│           ├── book_detail.html    ← Single book + add author
│           ├── authors.html        ← Author list + add form
│           └── author_detail.html  ← Single author + add book
├── book_authours_temps/
│   └── urls.py            ← Main URL config
└── manage.py
```

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install Django
pip install django

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the server
python manage.py runserver
```

---

## 🔗 URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/books/` | `books_page` | Show all books + add book form |
| `/books/create/` | `create_book` | Handle POST — save new book |
| `/books/<id>/` | `book_detail` | Show single book + its authors |
| `/books/<id>/add_author/` | `add_author_to_book` | Link an author to a book |
| `/authors/` | `authors_page` | Show all authors + add author form |
| `/authors/create/` | `create_author` | Handle POST — save new author |
| `/authors/<id>/` | `author_detail` | Show single author + their books |
| `/authors/<id>/add_book/` | `add_book_to_author` | Link a book to an author |

---

## 🧠 Models

```python
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    notes      = models.TextField(blank=True)

class Book(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    authors     = models.ManyToManyField(Author, related_name="books")
```

> 🔑 `ManyToManyField` means one book can have many authors, and one author can have many books.

---

## 💡 Key Concepts Used

| Concept | Where |
|---------|-------|
| `ManyToManyField` | `models.py` — links Books ↔ Authors |
| `.add()` | `views.py` — adds a relation without replacing existing ones |
| `.exclude()` | `views.py` — BONUS: filters out already-linked records |
| `get_object_or_404` | `views.py` — safely fetch by ID or return 404 |
| `{% csrf_token %}` | All forms — Django security requirement |
| `{% if available_authors %}` | `book_detail.html` — hide form if no options left |

---

## 🌟 BONUS Feature

The dropdown menus only show authors/books that are **not yet linked** to the current book/author.

```python
# In book_detail view — exclude already-linked authors
authors_not_in_book = Author.objects.exclude(books=book)

# In author_detail view — exclude already-linked books
books_not_with_author = Book.objects.exclude(authors=author)
```

---

## 👨‍💻 Author

**Ahmad** — Full Stack Development Student @ AXSOS Academy