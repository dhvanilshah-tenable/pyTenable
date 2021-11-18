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
        data_dict = copy.deepcopy(data)

        for key, value in data.items():
            if isinstance(value, bool):
                if value:
                    data_dict[key] = 1
                else:
                    data_dict.pop(key)
        data_dict.pop("id")
        return data_dict
