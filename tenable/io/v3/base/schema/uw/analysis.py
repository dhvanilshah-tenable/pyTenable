'''
Base Universal Workspace Analysis Schema
'''
from marshmallow import Schema, fields, validate as v
from .filters import FilterSchema


class AnalysisSchema(Schema):
    '''
    Schema supporting the base analysis structure
    '''
    filter = fields.Nested(FilterSchema)
    template = fields.Str()
    parameters = fields.Dict()
