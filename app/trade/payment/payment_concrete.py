from .interface.payment_interface import PaymentAbstract    
from main.models import UserModel
from book.models import BookModel
from services import att_trade_status
from book.services import att_book_status
from services.delete_other_offerts_trade import delete_others_trade

class Payment(PaymentAbstract): 
    """ a strategy to represent a payment method """
    def __init__(
            self,                                                                               
            payment_method: PaymentAbstract,  
            user: UserModel,
            book: BookModel,
            trade,
            *args, **kwargs ) -> None:
        self.payment_method = payment_method( #instancio seja qual for a implementação com os parâmetro tmb
            user=user,
            book=book,
            trade=trade)
        
        self.user = user
        self.book = book
        self.trade = trade
        
    def __str__(self):
        return f'{self.get_description()} - {self.get_code()}'

    @property
    def method(self) -> PaymentAbstract:
        return self.payment_method
    
    @method.setter
    def method(self, method:PaymentAbstract) -> None:
        self.payment_method = method

    @property
    def trade_value(self):
        return self.payment_method.trade_value

    def get_code(self, *args, **kwargs) -> str:
        return self.payment_method.get_code(*args, **kwargs)
    
    def get_description(self, *args, **kwargs) -> str:
        return self.payment_method.get_description(*args, **kwargs)
    
    def process_payment(self, *args, **kwargs):
        self.payment_method.process_payment(*args, **kwargs)
        self.validate_payment()
        self.confirmation_payment()

    def validate_payment(self, *args, **kwargs):
        if self.user == self.book.owner:
            raise ValueError('O usuário não pode trocar seu próprio livro')

    def confirmation_payment(self, *args, **kwargs):
        ...        
            #algum método comum entre as duas implementações
            #não retornar esse método para a classe de implementacao

    def confirmation_trade(self, *args, **kwargs):
        self.payment_method.confirmation_trade(*args, **kwargs)
        att_trade_status(self.trade, status="AC")
        att_book_status(book=self.book, status=False) 
        delete_others_trade(book=self.book, instance_exclude=self.trade) #when user agree with this trade, there other trades nedde be deleted
        

    
    def finalizate_payment(self, *args, **kwargs):
        """ return a flag if users nedded waiting the other user post own book """
        return self.payment_method.finalizate_payment(*args, **kwargs)

    def cancel_payment(self, *args, **kwargs):
        return self.payment_method.cancel_payment(*args, **kwargs)
