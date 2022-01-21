from marshmallow import Schema, fields


class FolderSchema(Schema):
    '''
    Schema for folder
    '''
    name = fields.Str()
