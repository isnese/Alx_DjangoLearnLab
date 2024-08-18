import django
import os

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None

if __name__ == "__main__":
    # Example usage
    print("Books by Author 'J.K. Rowling':")
    books = query_books_by_author('J.K. Rowling')
    if books:
        for book in books:
            print(book.title)
    else:
        print("No books found for the given author.")

    print("\nBooks in Library 'Central Library':")
    books = list_books_in_library('Central Library')
    if books:
        for book in books:
            print(book.title)
    else:
        print("No books found in the given library.")

    print("\nLibrarian for Library 'Central Library':")
    librarian = retrieve_librarian_for_library('Central Library')
    if librarian:
        print(librarian.name)
    else:
        print("No librarian found for the given library.")
