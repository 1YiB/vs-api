from typing import Any
import httpx
import orjson as json



def search(query:str,size:int,category:str,sortBy: str,sortOrder:str,client:httpx.Client) -> tuple[Any, int]:


    endpoint = f"/-/search?query={query}&size={size}&category={category}&sortBy={sortBy}&sortOrder={sortOrder}"
    r = client.get(url=endpoint)
    return (json.loads(r.content),r.status_code)
