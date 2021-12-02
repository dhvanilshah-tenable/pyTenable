import responses

WAS_FOLDERS_BASE_URL = 'https://cloud.tenable.com/api/v3/folders'
SAMPLE_FOLDER_ID = '178fe279-4e37-49ee-a5dc-8a447dd7043a'
SAMPLE_FOLDER = {
    'folder_id': SAMPLE_FOLDER_ID,
    'name': 'Folder name'
}


@responses.activate
def test_create(api):
    responses.add(
        responses.POST,
        f'{WAS_FOLDERS_BASE_URL}/webapp',
        json=SAMPLE_FOLDER
    )
    folder = api.v3.was.folders.create(SAMPLE_FOLDER['name'])
    assert isinstance(folder, dict)
    assert folder['folder_id'] == SAMPLE_FOLDER_ID


@responses.activate
def test_delete(api):
    responses.add(
        responses.DELETE,
        f'{WAS_FOLDERS_BASE_URL}/{SAMPLE_FOLDER_ID}/webapp'
    )
    resp = api.v3.was.folders.delete(SAMPLE_FOLDER_ID)
    assert resp is None


@responses.activate
def test_edit(api):
    payload = SAMPLE_FOLDER
    new_name = 'updated name'
    payload['name'] = new_name
    responses.add(
        responses.PUT,
        f'{WAS_FOLDERS_BASE_URL}/{SAMPLE_FOLDER_ID}/webapp',
        json=SAMPLE_FOLDER,
    )
    resp = api.v3.was.folders.edit(SAMPLE_FOLDER_ID, new_name)
    assert resp == SAMPLE_FOLDER


@responses.activate
def test_list(api):
    responses.add(
        responses.GET,
        f'{WAS_FOLDERS_BASE_URL}/webapp',
        json=[SAMPLE_FOLDER],
    )
    resp = api.v3.was.folders.list()
    assert resp == [SAMPLE_FOLDER]
