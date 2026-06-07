from django.urls import path
from .import views

urlpatterns = [
	path('books/', views.books_page, name='books'),
	path('books/create/', views.create_book, name='create_book'),
	path('books/<int:book_id>/', views.book_detail, name='book_detail'),
	path('books/<int:book_id>/add_author/', views.add_author_to_book, name='add_book_to_author'),


	path('authors/', views.authors_page, name='authors'),
	path('authors/create/', views.create_author, name='create_author'),
	path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
	path('authors/<int:author_id>/add_book/', views.add_book_to_author, name='add_book_to_author'),
]