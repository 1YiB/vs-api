# type:ignore
from jsonobject import (
    JsonObject,
    IntegerProperty,
    ListProperty,
    StringProperty,
    ObjectProperty,
    DecimalProperty,
)


class search_files(JsonObject):

    download = StringProperty()
    manifest = StringProperty()
    readme = StringProperty()
    changelog = StringProperty()
    icon = StringProperty()


class extension(JsonObject):

    name = StringProperty()
    displayName = StringProperty()
    desc = StringProperty()
    version = StringProperty()
    avgRating = DecimalProperty()
    downloadCount = IntegerProperty
    files = ObjectProperty(search_files)


class search(JsonObject):
    totalSize = IntegerProperty()
    extensions = ListProperty(ObjectProperty(extension))
