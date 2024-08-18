import django
import os
from django.conf import settings
from relationship_app.models import Author, Book, Library, Librarian

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(f'Book Title: {book.title}')

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f'Book Title: {book.title}')

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f'Librarian Name: {librarian.name}')

if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':")
    query_books_by_author('J.K. Rowling')
    
    print("\nBooks in Library 'Central Library':")
    list_books_in_library('Central Library')

    print("\nLibrarian for Library 'Central Library':")
    retrieve_librarian_for_library('Central Library')
