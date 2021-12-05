'''
Base Explore Search Schema
'''
from marshmallow import Schema
from marshmallow import fields as marshm_fields
from marshmallow import validate as v

from .filters import FilterSchema


class SortSchema(Schema):
    '''
    Schema for the sorting sub-object
    '''
    property = marshm_fields.Str()
    order = marshm_fields.Str(validate=v.OneOf(['asc', 'desc']))


class SearchSchema(Schema):
    '''
    Schema supporting the search request
    '''
    fields = marshm_fields.List(marshm_fields.Str(), allow_none=True,
                                default=None)
    filter = marshm_fields.Nested(FilterSchema, allow_none=True, default=None)
    limit = marshm_fields.Int(default=1000)
    next = marshm_fields.Int(allow_none=True)
    sort = marshm_fields.List(marshm_fields.Dict(), allow_none=True,
                              default=None)
