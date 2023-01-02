# type: ignore
from jsonobject import (
    JsonObject,
    StringProperty,
    DecimalProperty,
    ObjectProperty,
    ListProperty,
)

class user(JsonObject):
    loginName = StringProperty()
    fullName = StringProperty()
    avatarUrl = StringProperty()
    homepage = StringProperty()
    provider = StringProperty()

class review(JsonObject):
    user=ObjectProperty(user)
    comment= StringProperty()
    rating = DecimalProperty()

class reviews(JsonObject):
    reviews = ListProperty(ObjectProperty(review))
