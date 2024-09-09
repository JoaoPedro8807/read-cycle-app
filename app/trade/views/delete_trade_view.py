from django.db.models.base import Model as Model
from ..models import TradeModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render  
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from ..payment import PaymentFactory, Payment
from ..zip_objects import zip_trade_payment_objects

@login_required 
@require_http_methods(['DELETE'])
def delete_trade_view(request, pk):
    trade = get_object_or_404(
        TradeModel.objects.user_trades_requests(user=request.user),
        pk=pk)
    
    if request.user not in (trade.book.owner, trade.user):
        messages.error(request, 'Você não tem permissão para deletar esse objeto.')
        return redirect('trade:user-trades')
    
    payment_method = PaymentFactory.create_payment_method(
        method_key=trade.payment_method)
    payment = Payment(
        payment_method=payment_method,
        user=request.user,
        book=trade.book,
        trade=trade)    
    payment.cancel_payment()

    trade.delete() # ----------------->             <-------------------------------------

    new_list = zip_trade_payment_objects(
        trades=TradeModel.objects.user_trades_requests(request.user),
        user=request.user
    )
    template_render = {
        'default': 'trade/render_trade.html',
        'profile': 'main/render_user_trades_table.html',
    }
    template_flag = request.headers.get('X-TEMPLATE', 'default')
    template = template_render.get(template_flag)

    return render(
        request,
        template,
        context={
            'itens': new_list, 
            'partial': True
        }
    )

