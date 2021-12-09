import responses

VM_FOLDERS_BASE_URL = 'https://cloud.tenable.com/api/v3/folders'
SAMPLE_FOLDER_ID = 18
SAMPLE_FOLDER = {
    'unread_count': 0,
    'custom': 0,
    'default_tag': 0,
    'type': 'main',
    'name': 'my scans',
    'id': SAMPLE_FOLDER_ID
}


@responses.activate
def test_create(api):
    '''
    Test vm folders create method
    '''
    responses.add(
        responses.POST,
        VM_FOLDERS_BASE_URL,
        json=SAMPLE_FOLDER
    )
    resp = api.v3.vm.folders.create(SAMPLE_FOLDER['name'])
    assert resp == SAMPLE_FOLDER_ID


@responses.activate
def test_delete(api):
    '''
    Test vm folders delete method
    '''
    responses.add(
        responses.DELETE,
        f'{VM_FOLDERS_BASE_URL}/{SAMPLE_FOLDER_ID}'
    )
    resp = api.v3.vm.folders.delete(SAMPLE_FOLDER_ID)
    assert resp is None


@responses.activate
def test_edit(api):
    '''
    Test vm folders edit method
    '''
    responses.add(
        responses.PUT,
        f'{VM_FOLDERS_BASE_URL}/{SAMPLE_FOLDER_ID}'
    )
    resp = api.v3.vm.folders.edit(SAMPLE_FOLDER_ID, "edit test")
    assert resp is None


@responses.activate
def test_list(api):
    '''
    Test vm folders list method
    '''
    responses.add(
        responses.GET,
        VM_FOLDERS_BASE_URL,
        json={'folders': [SAMPLE_FOLDER]},
    )
    resp = api.v3.vm.folders.list()
    assert resp == [SAMPLE_FOLDER]
