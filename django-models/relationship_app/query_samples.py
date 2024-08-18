import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f'Author "{author_name}" does not exist.')

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f'Library "{library_name}" does not exist.')

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(librarian.name)
    except Library.DoesNotExist:
        print(f'Library "{library_name}" does not exist.')
    except Librarian.DoesNotExist:
        print(f'Librarian for library "{library_name}" does not exist.')

# Example usage
if __name__ == '__main__':
    print("Books by Author:")
    books_by_author('J.K. Rowling')
    
    print("\nBooks in Library:")
    books_in_library('Central Library')
    
    print("\nLibrarian for Library:")
    librarian_for_library('Central Library')
