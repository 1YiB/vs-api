from typing import Any
import httpx
import orjson as json


def reviews(uid:str,client:httpx.Client) -> tuple[Any, int]:

    endpoint = f"{uid}/reviews"
    r = client.get(url=endpoint)
    return (json.loads(r.content),r.status_code)
