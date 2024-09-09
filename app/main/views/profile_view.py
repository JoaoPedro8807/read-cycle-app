from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from book.models import BookModel
from trade.models import TradeModel
from trade.zip_objects import zip_trade_payment_objects
from ..forms import UserInfoForm
from django.db.models import Q, Count


UserModel = get_user_model()    


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        books = BookModel.objects.users_books(user=self.request.user)
        trades = TradeModel.objects.user_trades_requests(user=request.user) #fazer filtro por dono da troca ou n
        trade_payment_zip = zip_trade_payment_objects(trades, self.request.user)

        user_stats = trades.aggregate(
                total_trades=Count('id'),
                total_accepted=Count('id', filter=Q(accepted=True)),
                total_canceled=Count('id', filter=Q(status="CN")) #fazer a migration para add canceled
        )
        user_form = UserInfoForm(instance=self.request.user)
        context = {
            'books': books,
            'itens': trade_payment_zip,
            'user_form': user_form,
            'user_stats': user_stats
        }
        return render(
            request=self.request, 
            template_name='main/profile.html', 
            context=context)

    def handle_no_permission(self):
        messages.error(self.request, 'Você precisa estar logado para acessar esta página.')
        return redirect(reverse('main:login-page'))    