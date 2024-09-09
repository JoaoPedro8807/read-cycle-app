from collections import defaultdict
from book.models import BookModel as Book
from main.models import UserModel as User
from .models import TradeModel
class TradeValidation:
    def __init__(self, user: User, book: Book, book_offer: Book = None) -> None:
        self.user = user
        self.book = book
        self.book_offer = book_offer
        self.errors = defaultdict(list)
        print('USER: ', self.user, 'BOOK: ', self.book)                                                 
        self.clean_validation()


    def clean_validation(self):
        self.clean_user_book()
        if self.book_offer:
            self.clean_book_offer()

        if self.errors:
            print('ERRORS; ', self.errors)
            raise ValueError(self.errors['error'][0])

    def clean_book_offer(self):
        if TradeModel.objects.all_trades().filter(
            book_offer=self.book_offer
        ).exists():
            self.errors['error'].append('Você já ofereceu esse livro em outra troca, escolha outro ou cancele a troca')

    def clean_user_book(self):
        if self.book.owner == self.user:
            self.errors['error'].append('Você não pode solicitar uma troca com seu próprio livro.')
