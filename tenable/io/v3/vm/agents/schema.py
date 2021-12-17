'''
Agents API Endpoint Schemas
'''
from marshmallow import Schema, fields


class AgentsSchema(Schema):
    '''
    Schema for agents API
    '''
    items = fields.List(fields.UUID)
