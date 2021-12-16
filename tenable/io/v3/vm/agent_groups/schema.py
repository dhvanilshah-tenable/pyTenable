'''
Agent Groups API Endpoint Schemas
'''
from marshmallow import Schema, fields


class AgentGroupsSchema(Schema):
    '''
    Schema for agent_groups API
    '''
    name = fields.Str()
    items_ = fields.List(fields.UUID(), data_key='items')
