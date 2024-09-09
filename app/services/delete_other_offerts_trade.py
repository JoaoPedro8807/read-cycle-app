def delete_others_trade(instance_exclude, book)-> None:
    from trade.models import TradeModel
    TradeModel.objects.trades_unfinished().filter(
        book=book
    ).exclude(id=instance_exclude.id).delete()
