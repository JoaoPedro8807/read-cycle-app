from ..models import BookModel

def att_book_status(book: BookModel, status:bool):
    book.available = status
    book.save()
    return book
    

