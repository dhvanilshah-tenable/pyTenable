'''
test filters
'''
import responses

WAS_FILTERS_BASE_URL = 'https://cloud.tenable.com/api/v3/definitions'
CONFIG_ID = '36adf672-0b08-43b5-a15f-6b32044f6b1f'
SCAN_ID = 'cade336b-29fb-4188-b42a-04d8f95d7de6'


@responses.activate
def test_scans_filters(api):
    '''
    Test scans_filters
    '''
    filters = {
        'filters': [
            {
                'name': 'started_at',
                'readable_name': 'started_at',
                'operators': ['lt', 'lte', 'gt', 'gte'],
                'control': {
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$',
                    'readable_regex': 'YYYY/MM/DD',
                }
            }
        ]
    }
    responses.add(
        responses.GET,
        f'{WAS_FILTERS_BASE_URL}/configs/{CONFIG_ID}/scans/was',
        json=filters
    )
    resp = api.v3.was.filters.scans_filters(CONFIG_ID)
    assert resp == filters['filters']


@responses.activate
def test_scan_configurations_filters(api):
    '''
    Test test_scan_configurations_filters
    '''
    filters = {
        'filters': [
            {
                'name': 'scans_status',
                'readable_name': 'scans_status',
                'operators': ['eq'],
                'control': {
                    'type': 'dropdown',
                    'list': [
                        'Never Run',
                        'pending',
                        'running',
                        'stopping',
                        'aborted',
                        'canceled',
                        'completed'
                    ],
                }
            }
        ]
    }
    responses.add(
        responses.GET,
        f'{WAS_FILTERS_BASE_URL}/configs/was',
        json=filters
    )
    resp = api.v3.was.filters.scan_configurations_filters()
    assert resp == filters['filters']


@responses.activate
def test_scan_vulnerabilities_filters(api):
    '''
    Test scan_vulnerabilities_filters
    '''
    filters = {
        'filters': [
            {
                'name': 'uri',
                'readable_name': 'uri',
                'operators': ['eq', 'match'],
                'control': {
                    'type': 'entry',
                    'regex': None,
                    'readable_regex': None
                }
            }
        ]
    }
    responses.add(
        responses.GET,
        f'{WAS_FILTERS_BASE_URL}/scans/{SCAN_ID}/vulnerabilities/was',
        json=filters
    )
    resp = api.v3.was.filters.scan_vulnerabilities_filters(SCAN_ID)
    assert resp == filters['filters']


@responses.activate
def test_user_templates_filters(api):
    '''
    Test user_templates_filters
    '''
    filters = {
        'filters': [
            {
                'name': 'template_name',
                'readable_name': 'template_name',
                'operators': ['eq', 'neq'],
                'control': {
                    'type': 'dropdown',
                    'list': [
                        'scan',
                        'overview',
                        'ssl_tls',
                        'config_audit',
                        'pci',
                        'api'
                    ]
                }
            }
        ]
    }
    responses.add(
        responses.GET,
        f'{WAS_FILTERS_BASE_URL}/user-templates/was',
        json=filters
    )
    resp = api.v3.was.filters.user_templates_filters()
    assert resp == filters['filters']


@responses.activate
def test_vulnerabilities_filters(api):
    '''
    Test vulnerabilities_filters
    '''
    filters = {
        'filters': [
            {
                'name': 'asset_id',
                'readable_name': 'asset_id',
                'operators': ['eq'],
                'control': None
            }
        ]
    }
    responses.add(
        responses.GET,
        f'{WAS_FILTERS_BASE_URL}/vulnerabilities/was',
        json=filters
    )
    resp = api.v3.was.filters.vulnerabilities_filters()
    assert resp == filters['filters']
