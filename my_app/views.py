from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author



def books_page(request):
	"" "" ""



	"" "" ""
	all_books = Book.objects.all()
	context = {
		"books": all_books
	}
	return render(request, 'my_app/books.html', context)

def create_book(request):
	"" "" ""

	"" "" ""

	if request.method == "POST":
		title = request.POST['title']
		description = request.POST['description']

		Book.objects.create(title=title, description=description)

	return redirect('books')



def book_detail(request, book_id):
	"" "" ""

	"" "" ""

	book = get_object_or_404(Book, id=book_id)

	#BONUS

	authors_not_in_book = Author.objects.exclude(books=book)

	context = {
		'book': book,
		'available_authors': authors_not_in_book
	}
	return render(request, 'my_app/book_detail.html', context)


def add_author_to_book(request, book_id):
	"" "" ""

	"" "" ""
	if request.method == 'POST':
		book = get_object_or_404(Book, id=book_id)
		author_id = request.POST['author_id']
		author = get_object_or_404(Author, id=author_id)

		book.authors.add(author)
	return redirect('book_detail', book_id=book_id)



def authors_page(request):
	"" "" ""

	"" "" ""
	all_authors = Author.objects.all()
	context = {
		'authors': all_authors
	}
	return render(request, 'my_app/authors.html', context)



def create_author(request):
	if request.method =='POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		notes = request.POST['notes']
		Author.objects.create(
			first_name=first_name,
			last_name=last_name,
			notes=notes
		)
	return redirect('authors')



def author_detail(request, author_id):
	"" "" ""

	"" "" ""
	author = get_object_or_404(Author, id-author_id)
	
	
	#BONUS:
	books_not_with_author = Book.objects.exclude(authors=author)

	context = {
		'author': author,
		'available_books': books_not_with_author
	}
	return render(request, 'my_app/author_detail.html', context)


def add_book_to_author(request, author_id):
	"" "" ""

	"" "" ""
	if request.method == 'POST':
		author = get_object_or_404(Author, id=author_id)
		book_id = request.POST['book_id']
		book = get_object_or_404(Book, id=book_id)

		author.books.add(book)

	return redirect('authors_detail', author_id=author_id)