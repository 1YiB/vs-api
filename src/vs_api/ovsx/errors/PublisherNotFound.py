from typing import Optional


class PublisherNotFound(Exception):
    def __init__(self, namespace: str, message: Optional[str]) -> None:
        self.namespace = namespace
        self.message = f"Namespace not found: {self.namespace}" or message
        super().__init__(self.message)
