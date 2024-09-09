from trade.models.base.trade_base_model import TradeBaseModel
from django.conf import settings

def att_trade_status(trade:TradeBaseModel, status:str):
    """ att trade status and change some trade flags  """
    status_list = list(settings.TRADE_STATUS_FLAGS)
    if status not in list(map(lambda x: x[0], status_list)):
        raise ValueError('status não permitido')
    
    if status == "AC":  #trade accepted flag
        trade.accepted = True
        
    if status == "FN":
        trade.finalizate = True

    trade.status = status
    trade.save()
    return trade    