import httpx

from . import api, errors, models, types

__all__ = ["OpenVSX"]

class OpenVSX:
    def __init__(
        self,
        base_url: str = "https://open-vsx.org/api/",
        headers=None,
        proxies=None,
    ) -> None:
        self.base_url = base_url
        self.headers = headers
        self.proxies= proxies
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            proxies=self.proxies,
        )


    def info(self, uid: str):

        uid = types.uid(uid)
        (data, code) = api.info(uid=uid.url(), client=self.client)

        if code == 404: raise errors.ExtensionNotFound(uid,None)

        res = models.info(data=data)
        return res


    def publisher(self, namespace: str):

        (data, code) = api.publisher(namespace, self.client)

        if code == 404: raise errors.PublisherNotFound(namespace,None)

        res = models.publisher(data=data)
        return res

    def reviews(self, uid: str):

        uid = types.uid(uid)
        (data, code) = api.reviews(uid.url(), self.client)

        if code == 404: raise errors.ExtensionNotFound(uid,None)

        res = models.reviews(data=data)
        return res

    def search(
        self,
        query: str ,
        size: int = 10,
        category: types.category = "",
        sortBy: types.sortBy = "",
        sortOrder: types.sortOrder = "",
    ):

        (data, code) = api.search(
            query, size, category, sortBy, sortOrder, self.client
        )

        res = models.search(data=data)
        return res
