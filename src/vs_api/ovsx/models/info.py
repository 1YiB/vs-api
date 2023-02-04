from dataclasses import dataclass



@dataclass
class info_base:

    name:str
    displayName:str

    namespace:str
    description:str

    version:str
    platform: str
    license:str

    publisher = {
        "loginName":str,
        "fullName":str,
        "avatar":str,
        "homepage":str
    }

    verified:bool
    preview:bool
    preRelease:bool
    unrelatedPublisher:bool
    namespaceAccess:str

    dependencies:list
    bundledExtensions:list

    classification={
    "tags":list,
    "kind":list,
    "categories":list
    },

    engine = {},

    urls = {
        "homepage":str,
        "repository":str,
        "bugs":str
    }
    rating = {
        "count":int,
        "avg":float
    }
    downloads = {
        "urls":dict[str,str],
        "count":int
    },
    files = {
        "icon":str,
        "download":str,
        "manifest":str,
        "readme":str,
        "changelog":str,
        "license":str
    }

class info:
    def __new__(cls,data):

        return info_base(
            name=data.get("name"),
            displayName=data.get("displayName"),
            namespace=data.get("namespace"),
            description=data.get("description"),
            version=data.get("version"),
            platform=data.get("targetPlatform"),
            license=data.get("license"),
            verified=data.get("verified"),
            preview=data.get("preview"),
            preRelease=data.get("preRelease"),
            unrelatedPublisher=data.get("unrelatedPublisher"),
            namespaceAccess=data.get("namespaceAccess"),
            dependencies=data.get("dependencies"),
            bundledExtensions=data.get("bundledExtensions")
        )
