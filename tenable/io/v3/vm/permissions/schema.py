'''
Permissions API Endpoint Schemas
'''
from marshmallow import Schema, fields


class PermissionSchema(Schema):
    '''
    Schema for update functions in permissions/api.py

    Args:
    '''
    acls = fields.List(fields.Dict())
