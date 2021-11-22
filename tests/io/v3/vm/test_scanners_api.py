"""
Testing the Scanners endpoints
"""
import random
import uuid

import pytest
import responses
from responses import matchers
from tenable.io.v3.vm.schema import ScannerEditSchema

SCANNER_BASE_URL = r"https://cloud.tenable.com/scanners"
BASE_URL = r"https://cloud.tenable.com"
SCANNER_ID = "12345"


@responses.activate
def test_scanner_details(api):
    scanner_uuid = str(uuid.uuid1())
    responses.add(
        responses.GET,
        f"{SCANNER_BASE_URL}/{SCANNER_ID}",
        json={
            "creation_date": 1635431656,
            "group": True,
            "id": 12345,
            "key": "random_key",
            "last_connect": "null",
            "last_modification_date": 1637162052,
            "license": "null",
            "linked": 1,
            "name": "Autoscaling WAS Scanners (Hyperwas only)",
            "network_name": "Default",
            "num_scans": 0,
            "owner": {
                "owner": "system",
                "owner_id": 123456,
                "owner_name": "system",
                "owner_uuid": "3bfcfb11-6c12-405b-b7ba-bbc705cd2a6e",
            },
            "pool": True,
            "scan_count": 0,
            "shared": 1,
            "source": "service",
            "status": "on",
            "timestamp": 1637654052,
            "type": "local",
            "user_permissions": 64,
            "uuid": scanner_uuid,
            "supports_remote_logs": False,
            "supports_webapp": True,
        },
    )
    status = api.v3.vm.scanners.details(SCANNER_ID)
    assert isinstance(status, dict)
    assert status["uuid"] == scanner_uuid


@responses.activate
def test_scanners_linking_key(api):
    """
    Test the linking_key function
    """
    key1 = "".join(random.choice("0123456789abcdefgh") for i in range(65))
    key2 = "".join(random.choice("0123456789abcdefgh") for i in range(65))
    base_key = "00000000-0000-0000-0000-00000000000000000000000000001"
    responses.add(
        responses.GET,
        f"{SCANNER_BASE_URL}",
        json={
            "scanners": [
                {
                    "id": "1",
                    "uuid": base_key,
                    "key": key1,
                },
                {"id": "2", "uuid": str(uuid.uuid1()), "key": key2},
            ]
        },
    )
    linking_key = api.v3.vm.scanners.linking_key()

    assert linking_key == key1


@pytest.mark.skip("API method NotImplemented in v3")
def test_scanners_allowed_scanners():
    """
    Test the allowed_scanners function
    """
    pass


@responses.activate
def test_scanners_control_scan(api):
    """
    Test the control_scan function
    """
    scanner_uuid = str(uuid.uuid1())
    action = "stop"
    responses.add(
        responses.POST,
        f"{SCANNER_BASE_URL}/{SCANNER_ID}/scans/{scanner_uuid}/control",
        match=[matchers.json_params_matcher({"action": action})],
    )
    assert None is api.v3.vm.scanners.control_scan(
        SCANNER_ID, scanner_uuid, action)


@responses.activate
def test_scanners_delete(api):
    """
    Test the delete function
    """
    responses.add(responses.DELETE, f"{SCANNER_BASE_URL}/{SCANNER_ID}")
    assert None is api.v3.vm.scanners.delete(SCANNER_ID)


@responses.activate
def test_scanners_edit(api):
    """
    Test the edit function
    """
    schema = ScannerEditSchema()
    kwargs = {"force_plugin_update": True, "force_ui_update": False}
    payload = schema.dump(schema.load(kwargs))
    responses.add(
        responses.PUT,
        f"{BASE_URL}/settings/{SCANNER_ID}",
        match=[matchers.json_params_matcher(payload)],
    )

    assert None is api.v3.vm.scanners.edit(
        SCANNER_ID, force_plugin_update=False)


@responses.activate
def test_scanners_get_aws_targets(api):
    """
    Test the get_aws_targets function
    """
    targets = ["target1", "target2"]
    responses.add(
        responses.GET,
        f"{SCANNER_BASE_URL}/{SCANNER_ID}/aws-targets",
        json={"targets": targets},
    )
    resp = api.v3.vm.scanners.get_aws_targets(SCANNER_ID)
    assert isinstance(resp, list)
    assert resp == targets


@responses.activate
def test_scanners_get_scanner_key(api):
    """
    Test the get_scanner_key function
    """
    key = "".join(random.choice("0123456789abcdefgh") for i in range(65))
    responses.add(
        responses.GET,
        f"{SCANNER_BASE_URL}/{SCANNER_ID}/key",
        json={"key": key}
    )
    resp = api.v3.vm.scanners.get_scanner_key(SCANNER_ID)
    assert resp == key


@responses.activate
def test_scanners_get_scans(api):
    """
    Test the get_scans function
    """
    responses.add(
        responses.GET,
        f"{SCANNER_BASE_URL}/{SCANNER_ID}/scans",
        json={"scans": ["scans1", "scans2"]},
    )
    resp = api.v3.vm.scanners.get_scans(SCANNER_ID)
    assert isinstance(resp, list)
    assert resp == ["scans1", "scans2"]


@pytest.mark.skip("API method NotImplemented in v3")
def test_scanners_search():
    """
    Test the search function
    """
    pass


@responses.activate
def test_scanners_list(api):
    """
    Test the list function
    """
    scanners_list = [
        {"id": "1", "uuid": str(uuid.uuid1()), "key": "key1"},
        {"id": "2", "uuid": str(uuid.uuid1()), "key": "key2"},
    ]
    responses.add(
        responses.GET, f"{SCANNER_BASE_URL}", json={"scanners": scanners_list}
    )
    resp = api.v3.vm.scanners.list()
    assert isinstance(resp, list)
    assert resp == scanners_list


@responses.activate
def test_scanners_toggle_link_state(api):
    """
    Test the toggle_link_state function
    """
    responses.add(
        responses.PUT,
        f"{SCANNER_BASE_URL}/{SCANNER_ID}/link",
        match=[matchers.json_params_matcher({"link": int(True)})],
    )
    assert None is api.v3.vm.scanners.toggle_link_state(SCANNER_ID, True)


@pytest.mark.skip("API method NotImplemented in v3")
def test_scanners_get_permissions():
    """
    Test the get_permissions function
    """
    pass


@pytest.mark.skip("API method NotImplemented in v3")
def test_scanners_edit_permissions():
    """
    Test the edit_permissions function
    """
    pass
