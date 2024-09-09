from .authenticate_abstract import Auth

class GenericAuth:
    """ a generic class to implements a generic system auth """
    def __init__(self, authenticator: Auth) -> None:
        self.authenticator = authenticator
        super().__init__()

    def make_authenticate(self, *args, **kwargs):
        return self.authenticator.authenticate(*args, **kwargs)

    def logout(self, *args, **kwargs):
        return self.authenticator.logout(*args, **kwargs)

