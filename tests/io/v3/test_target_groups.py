"""
Testing the exports endpoints
"""
import responses
import pytest

RE_BASE = 'https://cloud.tenable.com/target-groups'
TARGET_GROUP = {
    "acls": [{
        "permissions": 16,
        "owner": 1,
        "display_name": "user2@example.com",
        "name": "user2@example.com",
        "id": 2,
        "type": "user"
    }],
    "owner": {
        "id": 2,
        "name": "user2@example.com",
    },
    "default_group": 0,
    "members": "192.0.2.53, 192.0.2.54, 192.0.2.55",
    "name": "RHEL_Hosts",
    "shared": 0,
    "user_permissions": 16,
    "last_modification_date": 1543622674,
    "creation_date": 1543622674,
    "id": 18
}


@responses.activate
def test_create(api):
    payload = TARGET_GROUP
    responses.add(responses.POST, RE_BASE, json=payload)
    resp = api.v3.vm.target_groups.create(name=payload['name'], members=payload["members"].split(", "),
                                          acls=payload['acls'])
    assert isinstance(resp, dict)
    assert resp['acls'] == payload['acls']
    assert resp['name'] == payload['name']
    assert resp['members'] == payload['members']


@responses.activate
def test_edit(api):
    id = '01234567-89ab-cdef-0123-4567890abcde'
    payload = TARGET_GROUP
    responses.add(responses.GET, f'{RE_BASE}/{id}', json=payload)

    updated_name = 'Updated TG Name'
    payload['name'] = updated_name
    responses.add(responses.PUT, f'{RE_BASE}/{id}', json=payload)

    resp = api.v3.vm.target_groups.edit(id, name=updated_name)

    assert isinstance(resp, dict)
    assert resp['acls'] == payload['acls']
    assert resp['name'] == payload['name']
    assert resp['members'] == payload['members']


@responses.activate
def test_delete(api):
    id = '01234567-89ab-cdef-0123-4567890abcde'
    responses.add(responses.DELETE, f'{RE_BASE}/{id}', json={})
    resp = api.v3.vm.target_groups.delete(id)
    assert resp is None


@responses.activate
def test_details(api):
    id = '01234567-89ab-cdef-0123-4567890abcde'
    responses.add(responses.GET, f'{RE_BASE}/{id}', json=TARGET_GROUP)
    jobs = api.v3.vm.target_groups.details(id)
    assert isinstance(jobs, dict)


@responses.activate
def test_search(api):
    response = {
        'target_groups': [TARGET_GROUP]
    }
    responses.add(responses.GET, RE_BASE, json=response)
    with pytest.raises(NotImplementedError) as error:
        resp = api.v3.vm.target_groups.search()
