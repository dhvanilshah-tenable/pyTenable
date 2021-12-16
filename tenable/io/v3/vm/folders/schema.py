'''
Folders API Endpoint Schemas
'''
from marshmallow import Schema, fields


class FoldersSchema(Schema):
    '''
    Schema for folders API
    '''
    name = fields.Str()
