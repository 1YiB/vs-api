import httpx
import simplejson as json
from ndicts.ndicts import NestedDict


from . import api  # done
from . import errors  # 3/4
from . import models  # 1/4
from . import types  # done

# [done] OpenVSX.info , OpenVSX.namespace , OpenVSX.reviews , OpenVSX.search -> [4/4]

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
        self.proxies = proxies
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            proxies=self.proxies,
        )

    def info(self, uid: str):
        uid = types.uid(uid)
        content, code = api.info(uid=uid.url(), client=self.client)

        match code:
            case 404:
                raise errors.ExtensionNotFound(uid, None)

            # TODO : more cases
            case _:
                nd = NestedDict(json.loads(content))

                res = models.info.info(
                    name=models.info.name(
                        trueName=nd.get(("name"),None),
                        displayName=nd.get(("displayName"),None),
                    ),
                    publisher=models.info.publisher(
                        org=models.info.org(
                            name=nd.get(("namespace"),None),
                            access=nd.get(("namespaceAccess"),None),
                            verified=nd.get(("verified"),None),
                            unrelated=nd.get(("unrelatedPublisher"),None),
                        ),
                        publishedBy=models.info.publishedBy(
                            loginName=nd.get(("publishedBy", "loginName"),None),
                            fullName=nd.get(("publishedBy", "fullName"),None),
                            avatar=nd.get(("publishedBy", "avatarUrl"),None),
                            homepage=nd.get(("publishedBy", "homepage"),None),
                            provider=nd.get(("publishedBy", "provider"),None),
                        ),
                    ),
                    metadata=models.info.metadata(
                        general=models.info.general(
                            desc=nd.get(("description"),None),
                            version=nd.get(("version"),None),
                            platform=nd.get(("targetPlatform"),None),
                            License=nd.get(("license"),None),
                            preview=nd.get(("preview"),None),
                            preRelease=nd.get(("preRelease"),None),
                        ),
                        classifcation=models.info.classifcation(
                            categories=nd.get(("categories"),None),
                            kind=nd.get(("extensionKind"),None),
                            tags=nd.get(("tags"),None),
                        ),
                        requirments=models.info.requirments(
                            engine=nd.get(("engines", "vscode"),None),
                            deps=nd.get(("dependencies"),None),
                            bundled=nd.get(("bundledExtensions"),None),
                        ),
                        rating=models.info.rating(
                            reviewCount=nd.get(("reviewCount"),None),
                            avg=nd.get(("averageRating"),None),
                        ),
                        downloads=models.info.downloads(
                            count=nd.get(("downloadCount"),None),
                        ),
                    ),
                    files=models.info.files(
                        download=nd.get(("files", "download"),None),
                        manifest=nd.get(("files", "manifest"),None),
                        readme=nd.get(("files", "readme"),None),
                        changelog=nd.get(("files", "changelog"),None),
                        icon=nd.get(("files", "icon"),None),
                    ),
                    urls=models.info.urls(
                        homepage=nd.get(("homepage"),None),
                        repo=nd.get(("repository"),None),
                        bugs=nd.get(("bugs"),None),
                    ),
                )
                return res

    def namespace(self, publisher: str):  #  -> models.namespace
        content, code = api.namespace(publisher, self.client)
        nd = NestedDict(json.loads(content))

        match code:
            case 404:
                raise errors.PublisherNotFound(publisher,None)
            case _:
                ext_res = []
                for extension in nd["extensions"]:
                    ext_res.append(
                        models.namespace.extension(
                            name=extension,
                            url=nd.get(("extensions",extension),None),
                        )
                    )
                res = models.namespace.namespace(
                    name=nd(('name'),None),
                    extensions=ext_res,
                    verified=nd(("verified"),None),
                    access=nd(("access"),None),
                )
                return res
    def reviews(self, uid: str):  # -> models.reviews
        uid = types.uid(uid)
        content, code = api.reviews(uid.url(), self.client)
        nd = NestedDict(json.loads(content))

        match code:
            case 404:
                raise errors.ExtensionNotFound(uid,None)
            case _:
                rev_res = []
                for review in nd['reviews']:
                    rev_res.append(
                        models.reviews.review(
                            user=models.reviews.user(
                                loginName= review.get(('user','loginName'),None),
                                fullName =review.get(('user','fullName'),None),
                                homepage=review.get(('user','homepage'),None),
                                provider =review.get(('user','provider'),None),
                            ),
                            comment=review.get(('comment'),None),
                            rating=review.get(('rating'),None),
                        )
                    )

                res = models.reviews.reviews(
                    reviews=rev_res
                )
                return res

    def search(
        self,
        query: str,
        size: int = 10,
        category: types.category = "",
        sortBy: types.sortBy = "",
        sortOrder: types.sortOrder = "",
    ):

        content, code = api.search(
            query, size, category, sortBy, sortOrder, self.client
        )
        nd = NestedDict(json.loads(content))

        ext_res = []
        for extension in nd["extensions"]:
            ext_res.append(
                models.search.extension(
                    name=extension.get(("name"),None),
                    displayName=extension.get(("displayName"),None),
                    desc=extension.get(("description"),None),
                    version=extension.get(("version"),None),
                    avgRating=extension.get(("averageRating"),None),
                    downloadCount=extension.get(("downloadCount"),None),
                    files=models.search.files(
                        download=extension.get(("files", "download"),None),
                        manifest=extension.get(("files", "manifest"),None),
                        readme=extension.get(("files", "readme"),None),
                        changelog=extension.get(("files", "changelog"),None),
                        icon=extension.get(("files", "icon"),None),
                    ),
                )
            )

        res = models.search.search(
            totalSize=nd.get(("totalSize"),None),
            extensions=ext_res
        )
        return res
