'''
Agent Groups API Endpoint Schemas
'''
from marshmallow import Schema, fields


class AgentGroupsBaseSchema(Schema):
    '''
    Schema for agent_groups API
    '''
    name = fields.Str()
    items = fields.List(fields.UUID)
