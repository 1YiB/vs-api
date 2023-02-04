from dataclasses import dataclass


@dataclass
class base_publisher:
    name:str
    extensions:dict[str,str]
    verified:bool
    access:str


class publisher:
    def __new__(cls,data):

        return base_publisher(
            name=data.get("name"),
            access=data.get("access"),
            extensions=data.get("extensions"),
            verified=data.get("verified"),
        )
