from django.views.generic import ListView
from ..models import TradeModel
from ..zip_objects import zip_trade_payment_objects
from django.contrib.auth.mixins import LoginRequiredMixin

class RequestsTradesView(LoginRequiredMixin, ListView):
    """ show for book owner, all trades on own book """
    model = TradeModel
    template_name = 'trade/requests_to_user.html'
    context_object_name = 'trades'

    def get_queryset(self):
        return TradeModel.objects.user_trades_requests(
            user=self.request.user)

    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        
        qs = self.get_queryset()
        if not qs:
            return context
        trades = zip_trade_payment_objects(
            trades=qs,
            user=self.request.user
        )
        context['trades'] = trades 
        return context 
    
