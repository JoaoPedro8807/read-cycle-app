from collections import defaultdict

class PaymentValidation:
    def __init__(self, data: type, errors: list = []) -> None:

        self.errors: list[str] = errors
        self.user = data.user
        self.data = data
        self.validate()


    def validate(self):
        self.validate_payment_value()
        self.validate_user_points()
        if self.errors:
            raise ValueError(self.errors[0])


    def validate_payment_value(self):
        value = int(self.data.trade_value) #set the real value is always dinamic, if book.value nedded change
        if not value in range(0, 101): #assume that the value of a book is always 100 points. If the value nedded change, change only verifications.
            self.errors.append('Pagamento inválido')

    def validate_user_points(self):
        points = int(self.data.trade_value)
        user_points = self.user.points
        print('USER: ', user_points, 'points: ', points)
        if not user_points >= points:
            self.errors.append('Usuário não possui pontos suficientes')