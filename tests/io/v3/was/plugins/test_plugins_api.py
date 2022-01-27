import requests
import responses

from tenable.io.v3.base.iterators.explore_iterator import (CSVChunkIterator,
                                                           SearchIterator)

WAS_PLUGINS_URL = 'https://cloud.tenable.com/api/v3/was/plugins'
ID = 1
PLUGIN = {
    'id': ID,
    'name': 'Scan Information',
    'risk_factor': 'info',
    'cpe': None,
    'cvss_vector': None,
    'cvss_base_score': None,
    'cvss3_vector': None,
    'cvss3_base_score': None,
    'cvss_score_source': None,
    'solution': None,
    'synopsis': 'Scan Information',
    'description': 'Provides scan information and statistics of plugins run.',
    'exploit_available': None,
    'see_also': [],
    'vuln_published': None,
    'patch_published': None,
    'plugin_published': '2017-03-31T00:00:00Z',
    'plugin_modified': '2017-03-31T00:00:00Z',
    'created_at': '2019-05-15T13:53:29.059Z',
    'updated_at': '2021-11-23T11:50:07.130781Z',
    'family': 'General',
    'policy': [],
    'wasc': [],
    'owasp': [],
    'cves': [],
    'owasp_asvs': [],
    'nist': [],
    'hipaa': [],
    'pci_dss': [],
    'iso': [],
    'capec': [],
    'disa_stig': [],
    'cwe': [],
    'bids': []
}

SEARCH_RESP = {
    'pagination': {
        'total': 2,
        'offset': 0,
        'limit': 10,
        'sort': [
            {
                'name': 'plugin_id',
                'order': 'asc',
            }
        ]
    },
    'items': [
        {
            'plugin_id': 98000,
            'name': 'Scan Information',
            'family': 'General',
            'policy': []
        },
        {
            'plugin_id': 98003,
            'name': 'OS Detection',
            'family': 'General',
            'policy': []
        }
    ]
}


@responses.activate
def test_details(api):
    '''
    Test was plugins plugin_details method
    '''
    responses.add(
        responses.GET,
        f'{WAS_PLUGINS_URL}/{ID}',
        json=PLUGIN
    )
    plugin = api.v3.was.plugins.details(ID)
    assert isinstance(plugin, dict)
    assert plugin == PLUGIN


@responses.activate
def test_search(api):
    '''
    Test was plugins search method
    '''

    fields = ['plugin_id',
              'name',
              'family',
              'policy']

    filters = {
        'and': [
            {
                'property': 'family',
                'operator': 'eq',
                'value': 'General'
            }
        ]
    }

    api_payload = {
        'fields': fields,
        'filter': filters,
        'limit': 2,
        'sort': [{'name': 'name', 'order': 'desc'}],
    }

    responses.add(
        responses.POST,
        f'{WAS_PLUGINS_URL}/search',
        json=SEARCH_RESP,
        match=[responses.matchers.json_params_matcher(api_payload)]
    )
    resp = api.v3.was.plugins.search(
        fields=fields,
        filter=filters,
        sort=[('name', 'desc')],
        limit=2
    )
    assert isinstance(resp, SearchIterator)

    for ind, folder in enumerate(resp):
        assert folder == SEARCH_RESP['items'][ind]

    resp = api.v3.was.plugins.search(
        fields=fields,
        filter=filters,
        sort=[('name', 'desc')],
        limit=2,
        return_csv=True
    )
    assert isinstance(resp, CSVChunkIterator)

    resp = api.v3.was.plugins.search(
        fields=fields,
        filter=filters,
        sort=[('name', 'desc')],
        limit=2,
        return_resp=True
    )
    assert isinstance(resp, requests.Response)
