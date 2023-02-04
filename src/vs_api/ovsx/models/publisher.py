from dataclasses import dataclass


@dataclass
class publisher_base:
    name:str
    extensions:dict[str,str]
    verified:bool
    access:str


class publisher:
    def __new__(cls,data) -> publisher_base:

        return publisher_base(
            name=data.get("name"),
            access=data.get("access"),
            extensions=data.get("extensions"),
            verified=data.get("verified"),
        )
