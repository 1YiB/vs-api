from typing import Any
import httpx
import orjson as json


def publisher(namespace:str,client:httpx.Client) -> tuple[Any, int]:

    endpoint = f"/{namespace}"
    r = client.get(url=endpoint)
    return (json.loads(r.content),r.status_code)
