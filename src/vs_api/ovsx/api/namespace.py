import httpx


def namespace(publisher:str,client:httpx.Client) -> tuple[bytes, int]:
    """
    returns list of published extensions for namespace

    Args:
        publisher (str): publisher namespace
        client (httpx.Client): httpx http client

    Returns:
        tuple[bytes,int]: tuple('api response','api status code')
    """

    endpoint = f"/{publisher}"
    r = client.get(url=endpoint)
    return (r.content,r.status_code)
