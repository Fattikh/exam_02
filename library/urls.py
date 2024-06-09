from django.urls import path
from library.views import *

app_name = 'library'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('authors/', authors, name='authors'),
    path('books/', books, name='books'),
    path('members/', members, name='members'),
    path('borrowing/', borrowing, name='borrowings'),
]