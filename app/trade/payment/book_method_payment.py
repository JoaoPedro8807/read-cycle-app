from .interface.payment_interface import PaymentAbstract
from main.models import UserModel
from book.models import BookModel
from book.services import att_book_status
from ..models.base.trade_base_model import TradeBaseModel
from services import att_trade_status
class BookTradePayment(PaymentAbstract):
    """ trade a book with a user's book """

    def __init__(self, 
            user:UserModel, 
            book:BookModel, 
            trade: TradeBaseModel
            ) -> None:   
        
        self.user = user    
        self.book = book
        self.trade = trade

    @property
    def trade_value(self, *args, **kwargs):
        return self.trade.book_offer
    
    @trade_value.setter
    def trade_value(self, book, *args, **kwargs):
        self.book = book

    @classmethod    
    def get_code(self):
        return "BT"
    
    @classmethod
    def get_description(self):
        return "Trocar por um de seus livros"       
    
    def process_payment(self,   *args, **kwargs):
        self.validate_payment()
        self.confirmation_payment()


    def validate_payment(self, *args, **kwargs):
        ...
        #chamar a class para limpar e validar o pagamento/trade

    def confirmation_payment(self, *args, **kwargs):
        offer_book = self.trade.book_offer
        trade_book = self.trade.book
        att_book_status(book=offer_book, status=False)
        att_book_status(book=trade_book, status=False)

    def confirmation_trade(self, *args, **kwargs):
        #colocar apenas metodos que são específico desse tippo de pagamento
        ...

    def finalizate_payment(self, post_code:str, *args, **kwargs) -> bool:
        """ return a flag if users nedded waiting the other user post own book """
        if self.trade.first_ship:
            att_trade_status(self.trade, status="FN")    
            return False 
        
        self.trade.first_ship = True #the owner confirmate is first
        att_trade_status(self.trade, status="FS")
        return True


    def cancel_payment(self, *args, **kwargs):  
        att_book_status(book=self.trade.book_offer, status=True)
        att_book_status(book=self.trade.book, status=True)

        #send email


    def register_post_code_user(self, trade: TradeBaseModel, post_code: str):
        trade = post_code
        trade.save()
        return trade
