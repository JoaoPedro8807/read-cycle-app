from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import TradeView, ConfirmationTradeView, RequestsTradesView, delete_trade_view, UserRequestsView, FinalizateTradeView, TradeSuccessView, TrackingView
import trade.views as views

app_name = 'trade'
urlpatterns = [
    path(
        '<uuid:id>',
        views.TradeView.as_view(),
        name='trade-index'
    ),
    path(
        '<uuid:id>/confirmate',
        views.ConfirmationTradeView.as_view(),
        name='trade-confirmate'
    ),
    path(
        'finalizate/<uuid:id>',
        views.FinalizateTradeView.as_view(),
        name='finalizate-trade'
    ),
    path(
        'minhas-trocas',
        views.UserRequestsView.as_view(),
        name='user-trades'
    ),
    path(
        'trocas-solicitadas',
        views.RequestsTradesView.as_view(),
        name='requests-trades-user'
    ),
    path(
        'delete/<uuid:pk>',
        views.delete_trade_view,
        name='delete-trade'
    ),

    path(
        'trade-success/<uuid:id>',
        views.TradeSuccessView.as_view(),
        name='trade-success-page'

    ),

    path(
        'tracking/<uuid:id>',
        views.TrackingView.as_view(),
        name='tracking-page'

    )


]
