'''
Testing the Permissions Schema
'''
from tenable.io.v3.vm.permissions.schema import PermissionSchema


def test_schema():
    schema = PermissionSchema()
    payload = schema.dump(schema.load(
        {'acls': [{'type': 'user', 'id': '2236706', 'permissions': 64}]}))
    assert payload == {
        'acls': [{'type': 'user', 'id': 2236706, 'permissions': 64}]}
