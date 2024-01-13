from .user import User

class MessageOrigin:
    def __init__(self) -> None:
        self.chatType: None | str
        self.id: None | int
        self.name: None | str
        self.fullName: None | tuple[str]

    def create(self, ctype: str, id: int, name: str | None, fname: None | tuple[str]):
        if ctype in ("PM", "GROUP"):
            self.chatType = ctype
        else:
            pass

        self.id = id
        self.name = name
        self.fullName = fname

class Message:
    _str = ''

    def __init__(self) -> None:
        self.id: None | int
        self.update: None | int
        self.author: None | User
        self.origin: None | MessageOrigin
        self.text: None | str

    def __repr__(self) -> str:
        return self._str if self.text is None else self.text

    def __str__(self) -> str:
        return self._str if self.text is None else self.text

    def create(self, id: int, update: int, author: User, origin: MessageOrigin, text: str):
        self.id = id
        self.update = update
        self.author = author
        self.origin = origin
        self.text = text
