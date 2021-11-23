"""
Testing the Groups endpoints
"""
import random
import uuid

import pytest
import responses
from responses import matchers

from tests.sc.conftest import group

GROUPS_BASE_URL = r"https://cloud.tenable.com/api/v3/groups"
BASE_URL = r"https://cloud.tenable.com"
GROUP_ID = "b27778c1-af10-4218-a1a4-c2c36b236e05"
USER_ID = "e9f23194-adb7-4c02-8632-615c694c787e"


@responses.activate
def test_add_user(api):
    responses.add(
        responses.POST,
        f"{GROUPS_BASE_URL}/{GROUP_ID}/users/{USER_ID}"
    )
    assert None is api.v3.groups.add_user(GROUP_ID, USER_ID)

@responses.activate
def test_create(api):
    group_name = "Test Group"
    responses.add(
        responses.POST,
        f"{GROUPS_BASE_URL}",
        match=[matchers.json_params_matcher({"name": group_name})],
        json={
            "id": GROUP_ID,
            "name": group_name,
        }
    )
    resp = api.v3.groups.create(group_name)
    assert group_name == resp["name"]
    assert GROUP_ID == resp["id"]

@responses.activate
def test_delete(api):
    responses.add(
        responses.DELETE,
        f"{GROUPS_BASE_URL}/{GROUP_ID}"
    )
    assert None is api.v3.groups.delete(GROUP_ID)

@responses.activate
def test_delete_user(api):
    responses.add(
        responses.DELETE,
        f"{GROUPS_BASE_URL}/{GROUP_ID}/users/{USER_ID}"
    )
    assert None is api.v3.groups.delete_user(GROUP_ID, USER_ID)

@responses.activate
def test_edit(api):
    updated_group_name = "Updated Test Group"

    responses.add(
        responses.PUT,
        f"{GROUPS_BASE_URL}/{GROUP_ID}",
        match=[matchers.json_params_matcher({"name": updated_group_name})],
        json={
            "id": GROUP_ID,
            "name": updated_group_name,
            "user_count": 0
        }
    )

    resp = api.v3.groups.edit(GROUP_ID, updated_group_name)
    assert GROUP_ID == resp["id"]
    assert updated_group_name == resp["name"]

@responses.activate
def test_list(api):
    responses.add(
        responses.POST,
        f"{GROUPS_BASE_URL}/search",
        match=[matchers.json_params_matcher({})],
        json={
            "groups": [
                {
                    "id": "b27778c1-af10-4218-a1a4-c2c36b236e05",
                    "name": "Test Group",
                    "user_count": 0,
                },
                {
                    "id": "00000000-0000-0000-0000-000000000000",
                    "immutable": True,
                    "membership_fixed": True,
                    "name": "All Users",
                    "role": "BASIC",
                    "user_count": 2,
                }
            ]
        }
    )

    resp = api.v3.groups.list()
    assert 2 == resp[1]["user_count"]
    assert "00000000-0000-0000-0000-000000000000" == resp[1]["id"]
    assert "Test Group" == resp[0]["name"]

@responses.activate
def test_list_users(api):

    responses.add(
        responses.GET,
        f"{GROUPS_BASE_URL}/{GROUP_ID}/users",
        json={
            "users": [
                {
                    "id": "e9f23194-adb7-4c02-8632-615c694c787e",
                    "username": "jyoti.patel@crestdatasys.com",
                    "email": "jyoti.patel@crestdatasys.com",
                    "name": "jyoti.patel@crestdatasys.com",
                    "type": "local",
                    "permissions": 64,
                    "login_fail_count": 0,
                    "login_fail_total": 0,
                    "last_apikey_access": 1636464654829,
                    "enabled": True,
                    "lockout": 0,
                    "lastlogin": 1635924062814

                },
                {
                    "id": "d3402235-7fa2-49e1-9a8f-15e97707c929",
                    "username": "tomeara@crestdatasys.com",
                    "email": "tomeara@crestdatasys.com",
                    "name": "tomeara@crestdatasys.com",
                    "type": "local",
                    "permissions": 64,
                    "login_fail_count": 0,
                    "login_fail_total": 0,
                    "enabled": True,
                    "lockout": 0
                }
            ]
        }
    )

    resp = api.v3.groups.list_users(GROUP_ID)
    assert "e9f23194-adb7-4c02-8632-615c694c787e" == resp[0]["id"]
    assert True == resp[0]["enabled"]
    assert "jyoti.patel@crestdatasys.com" == resp[0]["name"]
