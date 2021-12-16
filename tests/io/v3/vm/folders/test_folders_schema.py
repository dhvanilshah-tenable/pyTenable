'''
Testing the Folders Schema
'''
from tenable.io.v3.vm.folders.schema import FoldersSchema

FOLDER_NAME = 'folder'
FOLDER = {
    'name': FOLDER_NAME
}


def test_folders_schema(api):
    schema = FoldersSchema()
    payload = schema.dump(schema.load(FOLDER))
    assert payload == FOLDER
