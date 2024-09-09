from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from book.models import BookModel
from django.shortcuts import get_object_or_404
from ..payment import Payment, PaymentFactory
from ..shipping import Shipping, ShippingFacotry
from ..models import TradeModel
from ..forms import ShippingForm
from django.http import HttpResponse
from ..payment import PaymentAbstract
from . import ConfirmationTradeView
from django.contrib.auth.mixins import LoginRequiredMixin

class FinalizateTradeView(ConfirmationTradeView):
    def get_payment_method(self, method_key:str ) -> PaymentAbstract:
        return PaymentFactory.create_payment_method(
            method_key=method_key)

    def get_trades_accepteds(self, trade_id: str) -> TradeModel:
        return get_object_or_404(
            TradeModel.objects.trades_accepted(),
            id=trade_id)
    
    def get(self, request, *args, **kwargs):
        trade = self.get_trades_accepteds(kwargs.get('id'))
        
        payment_method = self.get_payment_method(trade.payment_method)
        payment = Payment(
            payment_method=payment_method,
            user=self.request.user,
            book=trade.book,
            trade=trade)

        shipping_form = ShippingForm()
        return render(
            request,
            'trade/finalizate_trade.html',
            context={
                'trade': trade,
                'payment': payment,
                'shipping_form': shipping_form
            }
        )

    def post(self, request, *args, **kwargs):
        shipping_method_key = request.POST.get('method', '')
        post_code = str(request.POST.get('cod', ''))
        trade = self.get_trades_accepteds(kwargs.get('id'))
        try:
            get_shipping = self.get_shipping_method(trade, request.user, post_code)
            shipping = Shipping(
                shipping=get_shipping['shipping_method'], 
                **get_shipping['params'])
            shipping.proccess_ship() #clean post_code

            if self.request.user == trade.book.owner:
                trade.owner_shipping_code = post_code
                trade.save()
            else:
                trade.user_shipping_code = post_code
                trade.save()
            
            payment_method = self.get_payment_method(trade.payment_method)
            payment = Payment(
                payment_method=payment_method,
                user=self.request.user,
                book=trade.book,
                trade=trade)
            
            await_trade = payment.finalizate_payment(post_code=post_code)#some payment_methods dont nedded await other user post own book, so i pass a callback to nedded methods (book_payment_method)

            if await_trade:
                messages.success(request, 'Envio verificado com sucesso, agora aguarde o outro usuário confirmar o envio.')
                return redirect('trade:trade-success-page', id=kwargs.get('id'))
            
            messages.success(request, 'Troca realizada com sucesso, PARABÉNS! Agora agurda até que os correios atualize o envio.')
            return redirect('trade:trade-success-page', id=kwargs.get('id'))

        except ValueError as error:
            messages.error(request, str(error))
            return redirect('trade:finalizate-trade', id=kwargs.get('id'))

class TradeSuccessView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trade = get_object_or_404(
            TradeModel.objects.trades_accepted(),
            id=kwargs.get('id')
        )
        payment_method = PaymentFactory.create_payment_method(
            method_key=trade.payment_method)
        payment = Payment(
            payment_method,
            request.user,
            trade.book, 
            trade)
        
        return render(
            request,
            'trade/confirmate_finalizate.html',
            context={
                'trade': trade,
                'payment': payment

            }
        )
