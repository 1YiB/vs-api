from typing import Any
import httpx
import orjson as json


def info(uid: str, client: httpx.Client) -> tuple[Any, int]:

    endpoint = uid
    r = client.get(url=endpoint)
    return (json.loads(r.content), r.status_code)
