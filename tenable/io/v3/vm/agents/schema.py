'''
Agents API Endpoint Schemas
'''
from marshmallow import Schema, fields


class AgentsBaseSchema(Schema):
    '''
    Schema for agents API
    '''
    items = fields.List(fields.UUID)
