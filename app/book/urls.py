from django.urls import path, include
from .views import (BookListView, BookView,  
                    MyBooksListView, 
                    ConfirmCreateBookView, 
                    DetailBookView, delete_book_view, 
                    AvaliationView)

    

app_name = 'book'
urlpatterns = [
    path(
        'list/',
        BookListView.as_view(),
        name='book-list-page'
    ),

    path(
        "create/", 
        BookView.as_view(), 
        name="book-create-page"
    ),
    path(
        'my-list/', 
        MyBooksListView.as_view(), 
        name='my-list-book-page'
    ),
    path(
        'create/confirm',
        ConfirmCreateBookView.as_view(),
        name='book-create-confirm'
    ),

    path(
        '<uuid:pk>/detail/',
        DetailBookView.as_view(),
        name='book-detail-page'
    ),     
    path(
        '<uuid:pk>/delete/',
        delete_book_view,
        name='book-delete-page'
    ),
    path(
        '<uuid:pk>/avaliation/',
        AvaliationView.as_view(),
        name='book-avaliation'
        )


]                                       

