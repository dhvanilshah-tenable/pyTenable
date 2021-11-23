"""
Testing the Scanner schemas
"""
import pytest
from tenable.io.v3.vm.schema import ScannerEditSchema
from marshmallow.exceptions import ValidationError


@pytest.fixture
def edit_payload():
    """
    Example scanner edit request
    """
    return {"force_plugin_update": True, "force_ui_update": False}


def test_scanner_edit_schema(edit_payload):
    """
    Test the vulnerability finding schema
    """
    test_resp = {"force_plugin_update": 1}
    schema = ScannerEditSchema()
    assert test_resp == schema.dump(schema.load(edit_payload))
