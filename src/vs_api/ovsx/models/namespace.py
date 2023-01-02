# type: ignore
from jsonobject import (
    JsonObject,
    StringProperty,
    BooleanProperty,
    ObjectProperty,
    ListProperty,
)


class extension(JsonObject):
    name = StringProperty()
    url = StringProperty()

class namespace(JsonObject):
    name = StringProperty()
    extensions = ListProperty(ObjectProperty(extension))
    verified = BooleanProperty()
    access = StringProperty()
