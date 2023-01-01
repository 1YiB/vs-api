import httpx

def info(uid: str, client: httpx.Client) -> tuple[bytes, int]:
    """
    returns info on extension

    Args:
        id (str): unique identifier of extension
        client (httpx.Client): httpx http client

    Returns:
        tuple[bytes, int]: tuple('api response','api status code')
    """

    endpoint = uid
    r = client.get(url=endpoint)
    return (r.content, r.status_code)
