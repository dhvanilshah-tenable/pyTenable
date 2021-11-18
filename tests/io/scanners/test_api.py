'''
Testing the Scanners endpoints
'''
from os import scandir
from uuid
import responses
import uuid
from tenable.io.v3.vm.schema import ScannerEditSchema



RE_BASE = (r'https://cloud.tenable.com/scanners')
scanner_resp = {}


@responses.activate
def test_details(api):
    scanner_uuid = str(uuid.uuid1())
    responses.add(responses.GET,
                  f"{RE_BASE}/12345",
                  json={
                    "creation_date": 1635431656,
                    "group": True,
                    "id": 12345,
                    "key": "b728328d82e9d533b5d4ba2240e7a939a263a11f92b7205ea72608cb62fc71bd",
                    "last_connect": "null",
                    "last_modification_date": 1637162052,
                    "license": "null",
                    "linked": 1,
                    "name": "Autoscaling WAS Scanners (Hyperwas only)",
                    "network_name": "Default",
                    "num_scans": 0,
                    "owner": "system",
                    "owner_id": 123456,
                    "owner_name": "system",
                    "owner_uuid": "3bfcfb11-6c12-405b-b7ba-bbc705cd2a6e",
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
                    "supports_webapp": True
                }
            )
    status = api.v3.vm.scanners.details(12345)
    # TODO: Add more assert conditions
    assert isinstance(status, dict)
    assert status["uuid"] == scanner_uuid

