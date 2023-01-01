import httpx

def search(query:str,size:int,category:str,sortBy: str,sortOrder:str,client:httpx.Client) -> tuple[bytes, int]:
    """
    returns info on extensions that match the query

    Args:
        query (str): search by name,desc or keywords
        size (int): no.of results to fetch
        category (str): category of extension to display
        sortBy (str): sorting of extensions
        sortOrder (str): sorting in ascending or descending
        client (httpx.Client): httpx http client

    Returns:
        tuple[bytes, int]: tuple('api response','api status code')
    """
    endpoint = f"/-/search?query={query}&size={size}&category={category}&sortBy={sortBy}&sortOrder={sortOrder}"
    r = client.get(url=endpoint)
    return (r.content,r.status_code)
