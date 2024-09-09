from collections import defaultdict

class PaymentValidation:
    def __init__(self, data: dict, errors: dict = {}) -> None:
        self.errors = errors or defaultdict(list)
        self.data = data
        self.validate()



    def validate(self):
        self.validate_payment_value()
        if self.errors:
            raise ValueError(self.errors)


    def validate_payment_value(self):
        value = self.data.get('value')
        # if float(value) not in range(0, 2000):
        #     raise ValueError('Valor muito acima do permitido')
