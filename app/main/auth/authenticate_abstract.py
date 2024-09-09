from abc import ABC, abstractmethod


class Auth(ABC):

    @abstractmethod
    def authenticate(self, *args, **kwargs):
        ...

    @abstractmethod
    def logout(self, *args, **kwargs):
        ...
        