"""
Testing the exports endpoints
"""
import re
import responses

RE_BASE = 'https://cloud.tenable.com/target-groups'


@responses.activate
def test_create(api):
    responses.add(responses.GET,
                  re.compile(f'{RE_BASE}/status'),
                  json={'uuid': '01234567-89ab-cdef-0123-4567890abcde',
                        'status': 'FINISHED',
                        }
                  )
    status = api.v3.vm.target_groups.create(name="test", members=["member1", "member2"], acls=[])
    assert isinstance(status, dict)
    assert status.uuid == '01234567-89ab-cdef-0123-4567890abcde'
    assert status.status == 'FINISHED'


@responses.activate
def test_edit(api):
    responses.add(responses.POST,
                  re.compile(f'{RE_BASE}/cancel'),
                  json={'status': 'CANCELLED'}
                  )
    assert 'CANCELLED' == api.exports.cancel(
        'vulns',
        '01234567-89ab-cdef-0123-4567890abcde'
    )


@responses.activate
def test_delete(api):
    id = "01234567-89ab-cdef-0123-4567890abcde"
    responses.add(responses.DELETE, f"{RE_BASE}/{id}", json={})
    resp = api.v3.vm.target_groups.delete(id)
    assert isinstance(resp, None)


@responses.activate
def test_details(api):
    response = {
        "acls": [
            {
                "permissions": 0,
                "owner": "NULL",
                "display_name": "NULL",
                "name": "NULL",
                "id": "NULL",
                "type": "default"
            },
            {
                "permissions": 128,
                "owner": 1,
                "display_name": "user2@example.com",
                "name": "user2@example.com",
                "id": 2,
                "type": "user"
            }
        ],
        "default_group": 0,
        "type": "user",
        "members": "192.0.2.53, 192.0.2.54, 192.0.2.55, 192.0.2.56, 192.0.2.57",
        "name": "Centos_Hosts",
        "owner": "user2@example.com",
        "shared": 0,
        "user_permissions": 128,
        "last_modification_date": 1543622642,
        "creation_date": 1543622642,
        "owner_id": 2,
        "id": 17
    }
    id = "01234567-89ab-cdef-0123-4567890abcde"
    responses.add(responses.GET, f"{RE_BASE}/{id}", json=response)
    jobs = api.v3.vm.target_groups.details(id)
    assert isinstance(jobs, dict)


@responses.activate
def test_list(api):
    response = {
        "target_groups": [
            {
                "acls": [
                    {
                        "permissions": 0,
                        "owner": "NULL",
                        "display_name": "NULL",
                        "name": "NULL",
                        "id": "NULL",
                        "type": "default"
                    },
                    {
                        "permissions": 128,
                        "owner": 1,
                        "display_name": "user2@example.com",
                        "name": "user2@example.com",
                        "id": 2,
                        "type": "user"
                    }
                ],
                "default_group": 0,
                "type": "user",
                "members": "192.0.2.53, 192.0.2.54, 192.0.2.55, 192.0.2.56, 192.0.2.57",
                "name": "Centos_Hosts",
                "owner": "user2@example.com",
                "shared": 0,
                "user_permissions": 128,
                "last_modification_date": 1543622642,
                "creation_date": 1543622642,
                "owner_id": 2,
                "id": 17
            }
        ]
    }
    responses.add(responses.GET, RE_BASE, json=response)
    target_groups = api.v3.vm.target_groups.list()
    assert isinstance(target_groups, list)
