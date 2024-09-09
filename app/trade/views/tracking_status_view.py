from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from book.models import BookModel
from django.shortcuts import get_object_or_404
from ..payment import Payment, PaymentFactory
from ..shipping import Shipping, ShippingFacotry
from ..models import TradeModel
from ..forms import ShippingForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class TrackingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trade = get_object_or_404(
            TradeModel.objects.trades_finished(),
            id=kwargs.get('id')
        )
        return render(
            request,
            'trade/tracking.html',
            context={
                'trade': trade
            }
        )