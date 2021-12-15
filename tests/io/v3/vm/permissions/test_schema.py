'''
Testing the Permissions Schema
'''
from tenable.io.v3.vm.permissions.schema import PermissionSchema


def test_schema():
    schema = PermissionSchema()
    payload = schema.dump(schema.load({'acls': [{}, {}]}))
    assert payload == {'acls': [{}, {}]}
