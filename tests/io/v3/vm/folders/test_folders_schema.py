'''
Testing the Folders Schema
'''
from tenable.io.v3.vm.folders.schema import FoldersBaseSchema

FOLDER_NAME = 'folder'
FOLDER = {
    'name': FOLDER_NAME
}


def test_folders_schema(api):
    schema = FoldersBaseSchema()
    payload = schema.dump(schema.load(FOLDER))
    assert payload == FOLDER
