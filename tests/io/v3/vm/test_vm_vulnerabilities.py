'''
Testing the VM Vulnerabilities endpoints actions
'''
import responses
from responses import matchers

from tenable.io.v3.vm.vulnerability import VulnerabilityIterator

VUL_BASE_URL = r'https://cloud.tenable.com/api/v3/findings/vulnerabilities'
BASE_URL = r'https://cloud.tenable.com/api/v3'


@responses.activate
def test_import_vulnerability(api):
    '''
    Test to validate Import Vulnerability action
    '''
    data = {
        'vendor': 'tenable',
        'product': 'tenable.sc',
        'data_type': 'vm',
        'source': '75c6c4c3-1626-4b57-9095-71b58ff8999e:\
            e9b89d18-87cc-4fd5-8e6f-27a1d24fa2ac0',
        'assets': [{
            'network_interfaces': {
                'ipv4': ['192.0.2.57', '192.0.2.177']
            },
            'hostname': 'windsmb.server.example.com',
            'bios_uuid': '9c60da51-762a-4b9b-8504-411056c2f696',
            'netbios_name': 'JUPITER',
            'vulnerabilities': [{
                'tenable_plugin_id': '97737',
                'last_found': 1568086236,
                'output': 'Description: The remote Windows host is \
                    missing a security update.'
            }]
        }]
    }

    responses.add(
        responses.POST,
        f"{BASE_URL}/findings/types/host",
        match=[matchers.json_params_matcher(data)],
        json={"job_uuid": ""}
    )
    resp = api.v3.vm.vulnerability.import_vulnerability(data)
    assert resp == {"job_uuid": ""}


@responses.activate
def test_search(api):
    '''
    Test the search functionality of Vulnerability API
    '''
    filter = ('id', 'eq', '00089a45-44a7-4620-bf9f-75ebedc6cc6c')
    fields = ["id"]
    limit = 2
    payload = {
        'fields': ['id'],
        'limit': 2,
        'sort': [],
        'filter': {
            'operator': 'eq',
            'property': 'id',
            'value': '00089a45-44a7-4620-bf9f-75ebedc6cc6c'
        }
    }
    response = {
        'findings': [{
            'id': '00089a45-44a7-4620-bf9f-75ebedc6cc6c',
            'asset': {},
            'definition': {
                'vpr': {},
                'cvss2': {},
                'cvss3': {},
                'references': [],
                'exploit_frameworks': []
            },
            'scan': {}
        }],
        'pagination': {
            'total': 1
        }
    }
    responses.add(
        responses.POST,
        f"{VUL_BASE_URL}/host/search",
        match=[matchers.json_params_matcher(payload)],
        json=response
    )

    resp = api.v3.vm.vulnerability.search(filter, fields=fields, limit=limit)
    assert isinstance(resp, VulnerabilityIterator)
    assert resp._payload == payload
    assert list(resp) == response.get("findings")
