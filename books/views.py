from django.views.generic import ListView, DetailView
from .models import Book



class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'  #to view the books which is inherited from List_View
    template_name = 'books/books_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

