from .interface.payment_interface import PaymentAbstract
from main.models import UserModel
from book.models import BookModel
from django.conf import settings
from .validations import PaymentValidation
from book.services import att_book_status
from decimal import  Decimal
from ..models.base.trade_base_model import TradeBaseModel
from services.delete_other_offerts_trade import delete_others_trade
from services import att_trade_status

class PointsTradePayment(PaymentAbstract):                                                              
    """ trade a book with a user's points
    """

    def __init__(self, 
            user:UserModel, 
            book:BookModel, 
            trade:TradeBaseModel
            ) -> None:
        
        self.user = user
        self.book = book 
        self.trade = trade


    @property
    def trade_value(self, *args, **kwargs):
        return self.trade.points_offer

    @staticmethod
    def get_code():
        return "PT"
    
    @staticmethod
    def get_description():
        return "Trocar por pontos"
    
    def process_payment(self, *args, **kwargs):
        self.validate_payment(*args, **kwargs)
        self.confirmation_payment(*args, **kwargs)

    def validate_payment(self, *args, **kwargs):
        ...
        PaymentValidation(data=self)

        #chamar aqui ou em outro lugar a task para enviar notificacao 
        #o book vai poder ter mais de uma requisição, então quando a uma requisição for aceita, as outras devem ser exlcuidas
         
    def confirmation_payment(self, *args, **kwargs):
        payment_value = self.trade_value
        self.user.sub_points(Decimal(payment_value))
        self.user.save()


    def confirmation_trade(self, *args, **kwargs):
        #colocar apenas metodos que são específico desse tippo de pagamento
        ...


    def finalizate_payment(self, post_code:str, *args, **kwargs):
        """ return a flag if users nedded waiting the other user post own book """
        self.trade.owner_post_code = post_code
        att_trade_status(trade=self.trade, status="FN")
        self.trade.save()
        return False
        #send email confirmation to above users

        #give 20 points to users to trade
        
    def cancel_payment(self, *args, **kwargs):
        self.trade.user.add_points(Decimal(self.trade_value))
        print('PRICE: ', self.trade_value, 'decimal: ', Decimal(self.trade_value))
        self.trade.user.save()
        att_book_status(book=self.book, status=True)
        self.trade.status = "CN"

        #att trade.status

        #send email cancel to above users
        ...



        

        

