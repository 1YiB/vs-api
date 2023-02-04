from typing import Optional


class ExtensionNotFound(Exception):
    def __init__(self, uid: str, message: Optional[str]) -> None:
        self.uid = uid
        self.message = f"Extension not found: {self.uid}" or message
        super().__init__(self.message)
