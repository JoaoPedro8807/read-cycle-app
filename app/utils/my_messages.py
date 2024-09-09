class Message:
    def __init__(self, msg: str, tags: str) -> str:
        self._msg = msg  
        self.tags = tags

    @property
    def msg(self) -> str:
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        self._msg = msg

    def __str__(self):
        return self._msg
    
    def __repr__(self) -> str:
        return self._msg