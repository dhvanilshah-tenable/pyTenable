'''
Folders Schema test
'''
from tenable.io.v3.was.folders.schema import FolderSchema


def test_folders_schema():
    '''
    Test FolderSchema
    '''
    schema = FolderSchema()
    payload = {'name': 'test_folder'}
    assert schema.dump(schema.load(payload)) == payload
