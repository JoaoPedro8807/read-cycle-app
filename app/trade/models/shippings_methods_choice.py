from ..shipping import CorreiosShipping

def get_all_shipping_methods_choice()-> list[tuple]:
    """ Return a list of tuple with all tpye of shipping to show in select choices model """
    METHODS = [CorreiosShipping('')]
    return [(method.get_shipping_code(), method.get_shipping_name()) for method in METHODS]