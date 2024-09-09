from ..payment import BookTradePayment, PointsTradePayment

def get_all_choice_payment_methods()-> list:
    """ Return a list of tuple to define payments_methods at the choices model """
    METHODS = [BookTradePayment, PointsTradePayment]
    return [(method.get_code(), method.get_description()) for method in METHODS]