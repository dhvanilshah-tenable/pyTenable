'''
Tests for search and filter schema
'''
import pytest
from marshmallow.exceptions import ValidationError

from tenable.io.v3.base.schema.explore import utils
from tenable.io.v3.base.schema.explore.filters import FilterSchema
from tenable.io.v3.base.schema.explore.search import SearchSchema, SortSchema

search_data = dict(
    fields=['bios_name', 'name'],
    filter=('bios_name', 'eq', 'SCCM'),
    limit=10,
    sort=[dict(property='bios_name', order='asc')],
    next='sdf000dfssdSDFSDFSFE00dfsdffaf'
)
sort_data = [('name', 'asc'), ('bios_name', 'desc')]
sort_data_schema = dict(property='bios_name', order='asc')


def test_search_schema():
    '''
    Test the users create schema
    '''
    test_resp = {
        'limit': 10,
        'fields': ['bios_name', 'name'],
        'next': 'sdf000dfssdSDFSDFSFE00dfsdffaf',
        'filter': {'value': 'SCCM',
                   'property': 'bios_name',
                   'operator': 'eq'},
        'sort': [{'property': 'bios_name', 'order': 'asc'}]
    }

    schema = SearchSchema()
    assert test_resp == schema.dump(schema.load(search_data))

    with pytest.raises(ValidationError):
        search_data['new_val'] = 'something'
        schema.load(search_data)


def test_sort_schema_generate():
    test_resp = [{'property': 'name', 'order': 'asc'},
                 {'property': 'bios_name', 'order': 'desc'}]
    sort_d = utils.generate_sort_data(sort_data)

    assert test_resp == sort_d


def test_sort_schema():
    test_resp = {'property': 'bios_name', 'order': 'asc'}
    schema = SortSchema()
    data = schema.dump(schema.load(sort_data_schema))
    assert test_resp == data


def test_filter_tuple_without_condition():
    tup_data = ('bios_name', 'eq', 'SCCM')
    test_resp = {'property': 'bios_name', 'operator': 'eq', 'value': 'SCCM'}
    schema = FilterSchema()
    data = schema.dump(schema.load(tup_data))

    assert test_resp == data


def test_filter_dict():
    tup_data = {'property': 'filter', 'operator': 'oper', 'value': 'value'}
    test_resp = {'operator': 'oper', 'value': 'value', 'property': 'filter'}
    schema = FilterSchema()
    data = schema.dump(schema.load(tup_data))

    assert test_resp == data


def test_filter_tuple_with_condition():
    tup_data = ('or', ('and', ('test', 'eq', '1'),
                       ('test', 'eq', '2')
                       ),
                'and', ('test', 'eq', 3)
                )
    test_resp = {
        'or': [
            {'and':
                [
                    {'operator': 'eq',
                     'value': '1',
                     'property': 'test'},
                    {'operator': 'eq',
                     'value': '2',
                     'property': 'test'}]}],
        'and': [{'operator': 'eq', 'value': 3, 'property': 'test'}]}
    schema = FilterSchema()
    data = schema.dump(schema.load(tup_data))

    assert test_resp == data
