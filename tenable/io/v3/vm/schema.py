import copy

from marshmallow import Schema, fields, post_dump
from marshmallow import validate as v


class ScannerEditSchema(Schema):
    """
    Schema for edit functions in scanners.py

    Args:

    """

    id = fields.Int(required=True)
    force_plugin_update = fields.Bool()
    force_ui_update = fields.Bool()
    finish_update = fields.Bool()
    registration_code = fields.Str()
    aws_update_interval = fields.Int()

    @post_dump
    def post_serialization(self, data, **kwargs):  # noqa PLR0201 PLW0613

        data = dict(filter(lambda item: item[1] != False, data.items()))

        data.update(map(lambda item: (item[0], 1) if item[1] == True else item, data.items()))

        data.pop("id")

        return data
