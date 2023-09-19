from marshmallow import Schema, fields


class MediumArticle(Schema):
    """
    Represents the schema for a Medium article. This is used to validate
    and deserialize the details of an article fetched from Medium.
    """

    title = fields.Str(required=True)
    pubDate = fields.DateTime(required=True)
    link = fields.Url(required=True)
    guid = fields.Url(required=True)
    author = fields.Str(required=True)
    thumbnail = fields.Url(required=True)
    description = fields.Str(required=True)
    content = fields.Str(required=True)
    categories = fields.List(fields.Str(), required=True)
    enclosure = fields.Dict()
