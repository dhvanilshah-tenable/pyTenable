'''
Test Filter
'''
import re

import responses

BASE_URL = 'https://cloud.tenable.com/filters'


@responses.activate
def test_agents_filters(api):
    '''
    Test case for filters agents_filters method
    '''
    test_response: dict = {
        'wildcard_fields': [
            'core_version',
            'distro',
            'groups'
        ],
        'filters': [
            {
                'name': 'core_version',
                'readable_name': 'Version',
                'operators': [
                    'eq',
                    'neq',
                    'match',
                    'nmatch'
                ],
                'control': {
                    'readable_regex': 'X.Y.Z',
                    'type': 'entry',
                    'regex': '.*'
                }
            },
            {
                'name': 'distro',
                'readable_name': 'Distro',
                'operators': [
                    'match',
                    'nmatch'
                ],
                'control': {
                    'readable_regex': 'Distro Name (e.g. es7-x86-64)',
                    'type': 'entry',
                    'regex': '.*'
                }
            },
            {
                'name': 'groups',
                'readable_name': 'Member of Group',
                'operators': [
                    'eq',
                    'neq'
                ],
                'control': {
                    'type': 'dropdown',
                    'list': [
                        {
                            'name': 'None',
                            'id': -1
                        },
                        {
                            'name': 'slibs',
                            'id': 106592
                        }
                    ]
                }
            }
        ],
        'sort': {
            'sortable_fields': [
                'core_version',
                'distro',
                'ip',
                'last_connect',
                'last_scanned',
                'name',
                'platform',
                'plugin_feed_id'
            ]
        }
    }
    responses.add(
        responses.GET,
        re.compile(f'{BASE_URL}/scans/agents'),
        json=test_response
    )
    res = api.v3.vm.filters.agents_filters()
    assert isinstance(res, dict)


@responses.activate
def test_credentials_filters(api):
    '''
    Test case for filters credentials_filters method
    '''
    test_response: dict = {
        'wildcard_fields': [
            'name',
            'description',
            'type'
        ],
        'filters': [
            {
                'name': 'name',
                'readable_name': 'Credential Name',
                'control': {
                    'readable_regex': 'TEXT',
                    'type': 'entry',
                    'regex': '.*'
                },
                'operators': [
                    'eq',
                    'neq',
                    'match',
                    'nmatch'
                ]
            },
            {
                'name': 'type',
                'readable_name': 'Credential Type',
                'control': {
                    'type': 'dropdown_multi',
                    'list': [
                        {
                            'id': 'Windows',
                            'name': 'Windows'
                        }
                    ]
                },
                'operators': [
                    'eq',
                    'neq'
                ]
            },
            {
                'name': 'created_date',
                'readable_name': 'Created Date',
                'control': {
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$',
                    'readable_regex': 'YYYY/MM/DD'
                },
                'operators': [
                    'date-lt',
                    'date-gt',
                    'date-eq',
                    'date-neq'
                ]
            }
        ],
        'sort': {
            'sortable_fields': [
                'name',
                'type',
                'created_date'
            ]
        }
    }
    responses.add(
        responses.GET,
        re.compile(f'{BASE_URL}/credentials'),
        json=test_response
    )
    res = api.v3.vm.filters.credentials_filters()
    assert isinstance(res, dict)


@responses.activate
def test_scan_filters(api):
    '''
    Test case for filters scan_filters method
    '''
    test_response: dict = {
        'filters': [
            {
                'name': 'host.id',
                'readable_name': 'Asset ID',
                'control': {
                    'type': 'entry',
                    'regex': '[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}'
                             '(,[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12})*',
                    'readable_regex': 'a94fd560-f8d9-4ed1-9b46-cba00c21bcdb'
                },
                'operators': [
                    'eq',
                    'neq',
                    'match',
                    'nmatch'
                ],
                'group_name': None
            },
            {
                'name': 'plugin.attributes.exploit_framework_canvas',
                'readable_name': 'CANVAS Exploit Framework',
                'control': {
                    'type': 'dropdown',
                    'list': [
                        'true',
                        'false'
                    ]
                },
                'operators': [
                    'eq',
                    'neq'
                ],
                'group_name': None
            },
            {
                'name': 'plugin.name',
                'readable_name': 'Plugin Name',
                'control': {
                    'type': 'entry',
                    'regex': '.*',
                    'readable_regex': 'TEXT'
                },
                'operators': [
                    'eq',
                    'neq',
                    'match',
                    'nmatch'
                ],
                'group_name': None
            }
        ]
    }
    responses.add(
        responses.GET,
        re.compile(f'{BASE_URL}/scans/reports'),
        json=test_response
    )
    res = api.v3.vm.filters.scan_filters()
    assert isinstance(res, dict)


@responses.activate
def test_scan_history_filters(api):
    '''
    Test case for filters scan_history_filters method
    '''
    test_response: dict = {
        'wildcard_fields': [

        ],
        'filters': [
            {
                'name': 'start_date',
                'readable_name': 'Start Date',
                'operators': [
                    'date-gt',
                    'date-lt',
                    'date-eq',
                    'date-neq'
                ],
                'control': {
                    'readable_regex': 'YYYY/MM/DD',
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
                }
            },
            {
                'name': 'end_date',
                'readable_name': 'End Date',
                'operators': [
                    'date-gt',
                    'date-lt',
                    'date-eq',
                    'date-neq'
                ],
                'control': {
                    'readable_regex': 'YYYY/MM/DD',
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
                }
            },
            {
                'name': 'status',
                'readable_name': 'Scan Status',
                'operators': [
                    'eq',
                    'neq',
                    'nmatch',
                    'match'
                ],
                'control': {
                    'readable_regex': 'TEXT',
                    'type': 'entry',
                    'regex': '.*'
                }
            }
        ],
        'sort': {
            'sortable_fields': [
                'start_date',
                'end_date',
                'status'
            ]
        }
    }
    responses.add(
        responses.GET,
        re.compile(f'{BASE_URL}/scans/reports/history'),
        json=test_response
    )
    res = api.v3.vm.filters.scan_history_filters()
    assert isinstance(res, dict)


@responses.activate
def test_workbench_asset_filters(api):
    '''
    Test case for filters workbench_asset_filters method
    '''
    test_response: dict = {
        'wildcard_fields': [

        ],
        'filters': [
            {
                'name': 'start_date',
                'readable_name': 'Start Date',
                'operators': [
                    'date-gt',
                    'date-lt',
                    'date-eq',
                    'date-neq'
                ],
                'control': {
                    'readable_regex': 'YYYY/MM/DD',
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
                }
            },
            {
                'name': 'end_date',
                'readable_name': 'End Date',
                'operators': [
                    'date-gt',
                    'date-lt',
                    'date-eq',
                    'date-neq'
                ],
                'control': {
                    'readable_regex': 'YYYY/MM/DD',
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
                }
            },
            {
                'name': 'status',
                'readable_name': 'Scan Status',
                'operators': [
                    'eq',
                    'neq',
                    'nmatch',
                    'match'
                ],
                'control': {
                    'readable_regex': 'TEXT',
                    'type': 'entry',
                    'regex': '.*'
                }
            }
        ],
        'sort': {
            'sortable_fields': [
                'start_date',
                'end_date',
                'status'
            ]
        }
    }
    responses.add(
        responses.GET,
        re.compile(f'{BASE_URL}/workbenches/assets'),
        json=test_response
    )
    res = api.v3.vm.filters.workbench_asset_filters()
    assert isinstance(res, dict)


@responses.activate
def test_workbench_vuln_filters(api):
    '''
    Test case for filters workbench_vuln_filters method
    '''
    test_response: dict = {
        'wildcard_fields': [

        ],
        'filters': [
            {
                'name': 'start_date',
                'readable_name': 'Start Date',
                'operators': [
                    'date-gt',
                    'date-lt',
                    'date-eq',
                    'date-neq'
                ],
                'control': {
                    'readable_regex': 'YYYY/MM/DD',
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
                }
            },
            {
                'name': 'end_date',
                'readable_name': 'End Date',
                'operators': [
                    'date-gt',
                    'date-lt',
                    'date-eq',
                    'date-neq'
                ],
                'control': {
                    'readable_regex': 'YYYY/MM/DD',
                    'type': 'datefield',
                    'regex': '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
                }
            },
            {
                'name': 'status',
                'readable_name': 'Scan Status',
                'operators': [
                    'eq',
                    'neq',
                    'nmatch',
                    'match'
                ],
                'control': {
                    'readable_regex': 'TEXT',
                    'type': 'entry',
                    'regex': '.*'
                }
            }
        ],
        'sort': {
            'sortable_fields': [
                'start_date',
                'end_date',
                'status'
            ]
        }
    }
    responses.add(
        responses.GET,
        re.compile(f'{BASE_URL}/workbenches/vulnerabilities'),
        json=test_response
    )
    res = api.v3.vm.filters.workbench_vuln_filters()
    assert isinstance(res, dict)
