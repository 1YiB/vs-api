import httpx

def reviews(uid:str,client:httpx.Client) -> tuple[bytes, int]:
    """
    returns all reviews of an extension

    Args:
        uid (str): extension unique identifier
        client (httpx.Client): httpx http client

    Returns:
        tuple[bytes, int]: tuple('api response','api status code')
    """

    endpoint = f"/{uid}/reviews"
    r = client.get(url=endpoint)
    return (r.content,r.status_code)
