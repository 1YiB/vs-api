# type: ignore
from jsonobject import (
    JsonObject,
    StringProperty,
    DecimalProperty,
    IntegerProperty,
    BooleanProperty,
    ObjectProperty,
    ListProperty,
)




class name(JsonObject):


    trueName = StringProperty()
    displayName = StringProperty()


### publisher sub classes ###

class org(JsonObject):

    name = StringProperty()
    access = StringProperty()
    verified = BooleanProperty()
    unrelated = BooleanProperty


class publishedBy(JsonObject):

    loginName = StringProperty()
    fullName = StringProperty()
    avatar = StringProperty()
    homepage = StringProperty()
    provider = StringProperty()


### publisher main class ###


class publisher(JsonObject):

    org = ObjectProperty(org)
    publishedBy = ObjectProperty(publishedBy)


### metadata sub classes ###


class general(JsonObject):

    desc = StringProperty()
    version = StringProperty()
    platform = StringProperty()
    License = StringProperty()
    preview = BooleanProperty()
    preRelease= BooleanProperty()

class classifcation(JsonObject):

    categories = ListProperty(str)
    kind = ListProperty(str)
    tags = ListProperty(str)


class requirments(JsonObject):

    engine = StringProperty()
    dep = ListProperty(str)
    bundled = ListProperty(str)


class rating(JsonObject):

    count = IntegerProperty()
    avg = DecimalProperty()


class downloads(JsonObject):

    count = IntegerProperty()


### metadata main class ###


class metadata(JsonObject):

    general = ObjectProperty(general)
    classifcation = ObjectProperty(classifcation)
    requirments = ObjectProperty(requirments)
    rating = ObjectProperty(rating)
    downloads = ObjectProperty(downloads)

## files main class ###

class files(JsonObject):

    download = StringProperty()
    manifest = StringProperty()
    readme = StringProperty()
    changelog = StringProperty()
    icon = StringProperty()

### urls main class ###

class urls(JsonObject):

    homepage = StringProperty()
    repo = StringProperty()
    bugs = StringProperty()


### info main class ###

class info(JsonObject):


    name = ObjectProperty(name)
    publisher = ObjectProperty(publisher)
    metadata = ObjectProperty(metadata)
    files = ObjectProperty(files)
    urls= ObjectProperty(urls)
