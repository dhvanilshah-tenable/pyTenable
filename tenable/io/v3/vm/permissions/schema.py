'''
Permissions API Endpoint Schemas
'''
from marshmallow import Schema, fields, validate


class PermissionAclSchema(Schema):
    '''
    Schema for acls for change permissions action
    '''
    type = fields.Str(required=True, validate=validate.OneOf(
        ['default', 'user', 'group']))
    id = fields.Int(required=True)
    permissions = fields.Int(required=True)


class PermissionSchema(Schema):
    '''
    Schema for update functions in permissions/api.py
    '''
    acls = fields.List(fields.Nested(PermissionAclSchema))
