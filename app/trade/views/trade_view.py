from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import View
from book.models import BookModel
from ..forms import CreateTradeForm
from ..payment import Payment, PaymentFactory, PaymentAbstract
from ..models import TradeModel
from ..shipping import ShippingFacotry, Shipping, ShippingAbstract
from django.conf import settings
from decimal import Decimal
from ..validations import TradeValidation
from django.contrib.auth.mixins import LoginRequiredMixin

class TradeView(LoginRequiredMixin, View):
    def get_book(self, book_id):
        return get_object_or_404(
            BookModel.objects.books_available(),
            id=book_id)

    def get_trade_form(self, user, post_data=None):
        if post_data:
            return CreateTradeForm(user=user, data=post_data)
        return CreateTradeForm(user=user)

    def create_trade(
            self, 
            book, 
            user, 
            payment_method_key, 
            shipping_method_key,
            *args,
            **kwargs ):
        return TradeModel.objects.create(
            book=book,
            user=user,
            payment_method=payment_method_key,
            shipping_method=shipping_method_key,
            **kwargs
        )
    
    def get_payment_method(self, method_key:str ) -> PaymentAbstract:
        return PaymentFactory.create_payment_method(
            method_key=method_key)


    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id', '')
        book = self.get_book(book_id)
        form = self.get_trade_form(request.user)
        return render(
            request,
            'trade/trade-index.html',
            context={
                'book': book,
                'form': form
            })

    def post(self, request, *args, **kwargs):
        book = self.get_book(kwargs.get('id', ''))
        form = self.get_trade_form(request.user, request.POST)

        if not form.is_valid():
            print('ERRO NO FORM: ', form.errors)
            messages.error(request=request, message=form.errors)
            return redirect('trade:trade-index', id=book.id)
        
        payment_method_key = request.POST.get('payment_method', 'PT')
        shipping_method_key = request.POST.get('shipping_method', 'CR')

        offer = {
            'PT':  {
                'points_offer': (book.price or Decimal(settings.DEFAULT_ANY_BOOK_PRICE)),
                'book_offer': None 
                },
            'BT': {
                'points_offer': None,
                'book_offer': (BookModel.objects.filter(
                    id=request.POST.get('offer_book')).first())
            },
        }
        offert = offer.get(payment_method_key)
        points_offer = offert['points_offer']
        book_offer = offert['book_offer']

        try:         
            TradeValidation(user=self.request.user, book=book, book_offer=book_offer)
            trade = self.create_trade(  
                book=book, 
                user=request.user, 
                payment_method_key=payment_method_key,
                shipping_method_key=shipping_method_key,
                book_offer=book_offer,
                points_offer=points_offer
                )
            payment_method = self.get_payment_method(trade.payment_method)
            payment = Payment(
                payment_method=payment_method,
                user=self.request.user, 
                book=trade.book,
                trade=trade)
            payment.process_payment()
            messages.success(self.request, 'Troca solicitada com sucesso, seus pontos já foramd descontados.\
                Agora aguarde o propietário confirmar a troca, caso ele não aceite dentro de 7 dias, seus pontos serão retornandos.')
            return redirect('trade:trade-confirmate', id=trade.id)

        except Exception as err:
            print('ERROR NO PROCESS: ', err)
            messages.error(request=request, message=f'Erro ao processar o pagamento: {str(err)}')
            return redirect('trade:trade-index', id=kwargs.get('id'))
        

class ConfirmationTradeView(LoginRequiredMixin, View):
    """Display trade confirmations for the book owned by the user."""
    def get_trade(self, trade_id):
        return get_object_or_404(
            TradeModel.objects.all().select_related('book', 'user'),
            id=trade_id
        )
    def get_shipping_method(self, trade: TradeModel, request_user, post_code: str = None) -> dict:
        params = {
            '_from': trade.book.owner.zip_code,
            '_to': trade.user.zip_code,
            'post_code': post_code
        }
        if request_user == trade.user: # o frete pode mudar de preço dependendo da ordem dos ceps
            params['_from'], params['_to'] = params['_to'], params['_from']

        shipping = ShippingFacotry.get_shipping_instance(
            method_key=trade.shipping_method
            )            
        return {
            'shipping_method': shipping,                                            
            'params': params
        }

    def get_payment_method(self, method_key:str ) -> PaymentAbstract:
        return PaymentFactory.create_payment_method(
            method_key=method_key)

    def get(self, request, *args, **kwargs):
        trade = self.get_trade(kwargs.get('id'))

        get_shipping = self.get_shipping_method(trade, request.user)
        shipping = Shipping(
            shipping=get_shipping['shipping_method'], 
            **get_shipping['params'])
        
        estimate_shipping_price = shipping.calculate_price_shipping()

        payment_method = self.get_payment_method(trade.payment_method)
        payment = Payment(
            payment_method=payment_method,
            user=self.request.user,
            book=trade.book,
            trade=trade)
        context = {
            'trade': trade,
            'payment_method': payment,
            'payment_value': payment.trade_value,  #rendered conditionaly on template
            'estimate_shipping_price': estimate_shipping_price
        }
        template = 'trade/trade-owner-confirmate.html'
        if request.user == trade.user:
            template = 'trade/trade-user-confirmate.html'
        
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        trade = self.get_trade(kwargs.get('id'))
        try:
            payment_method = self.get_payment_method(trade.payment_method)
            payment = Payment(
                payment_method=payment_method,
                user=self.request.user,
                book=trade.book,
                trade=trade)
            payment.confirmation_trade()
            return redirect('trade:finalizate-trade', id=trade.id)

        except Exception as err:
            print('ERRO NO TRADE CONFIRMATE: ', err)
            return redirect('trade:trade-confirmate', id=trade.id)
