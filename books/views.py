from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book



class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'  #to view the books which is inherited from List_View.
    template_name = 'books/books_list.html'
    login_url = 'account_login'  #for authorized login access to view booklistview.

class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/books_list.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
