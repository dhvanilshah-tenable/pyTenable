'''
Folders API Endpoint Schemas
'''
from marshmallow import Schema, fields


class FoldersBaseSchema(Schema):
    '''
    Schema for folders API
    '''
    name = fields.Str()
