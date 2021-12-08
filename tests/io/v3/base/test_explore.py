'''
Testing the search endpoint
'''

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.base.iterators.search_iterator import SearchIterator

REQUESTDATA = dict(
    fields=['test1', 'test2'],
    filter=('netbios_name', 'eq', 'SCCM'),
    limit=10,
    sort=[('name', 'asc')]
)


def test_search(api):
    search_iterator = ExploreBaseEndpoint(
        api).search(
        resource='assets',
        api_path='api/v3/assets/search',
        **REQUESTDATA
    )
    assert isinstance(search_iterator, SearchIterator)
