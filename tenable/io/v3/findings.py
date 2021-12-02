'''
Findings
=========

The following methods allow for interaction into the Tenable.io
:devportal:`vulnerabilities <vulnerabilities>` API.

Methods available on ``tio.v3.findings``:

.. rst-class:: hide-signature
.. autoclass:: FindingsAPI
    :members:
'''
from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.base.iterators.search_iterator import SearchIterator
from tenable.io.v3.base.schema.explore.filters import FilterSchema
from tenable.io.v3.base.schema.explore.search import SearchSchema
from tenable.io.v3.base.schema.explore.utils import generate_sort_data

class FindingsIterator(SearchIterator):
    '''
    Findings iterator
    '''
    pass
    
class FindingsAPI(ExploreBaseEndpoint):
    
    '''
    '''
    _path = 'api/v3/findings'
    _conv_json = True
    
    def search(self, *filters, **kw) -> FindingsIterator:
        '''
        Retrieves the assets.
        Requires -
            fields -- list of string = ['field1', 'field2'] -> fields is not supported by the search_assets api
            filter -- tuple ('field_name', 'operator', 'value') -- ('and', ('test', 'oper', '1'), ('test', 'oper', '2'))
            sort -- 'sort': [
                        {'last_observed': 'desc'}
                    ]
            limit -- integer = (10)
            next -- str = ('adfj3u4j34u9j48wi3j5w84jt5') -> next token
        Returns:
            Iterable:
                The iterable that handles the pagination and potentially
                async requests for the job.
        '''

        filter_schema = FilterSchema()
        search_schema = SearchSchema()
        query = filter_schema.dump(filter_schema.load(filters[0]))
        sort_data = generate_sort_data(kw, is_with_prop=False)
        kw.update({'filter': query,
                   'sort': sort_data})
        payload = search_schema.dump(search_schema.load(kw))
        return FindingsIterator(
            api=self,
            _limit=payload['limit'],
            _path='vulnerabilities/webapp/search',
            _resource='findings',
            _payload=payload
        )