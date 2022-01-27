import requests
import responses

from tenable.io.v3.base.iterators.explore_iterator import (CSVChunkIterator,
                                                           SearchIterator)

WAS_FOLDERS_URL = 'https://cloud.tenable.com/api/v3/was/folders'
FOLDER_ID = '178fe279-4e37-49ee-a5dc-8a447dd7043a'
FOLDER = {
    'unread_count': 0,
    'custom': 0,
    'default_tag': 0,
    'type': 'trash',
    'name': 'Trash',
    'id': FOLDER_ID
}


@responses.activate
def test_create(api):
    '''
    Test was folders create method
    '''
    resp = {
        'id': FOLDER_ID
    }
    responses.add(
        responses.POST,
        WAS_FOLDERS_URL,
        json=resp
    )
    folder = api.v3.was.folders.create(FOLDER['name'])
    assert isinstance(folder, dict)
    assert folder['id'] == FOLDER_ID


@responses.activate
def test_delete(api):
    '''
    Test was folders delete method
    '''
    responses.add(
        responses.DELETE,
        f'{WAS_FOLDERS_URL}/{FOLDER_ID}'
    )
    resp = api.v3.was.folders.delete(FOLDER_ID)
    assert resp is None


@responses.activate
def test_edit(api):
    '''
    Test was folders edit method
    '''
    payload = FOLDER
    new_name = 'updated name'
    payload['name'] = new_name
    responses.add(
        responses.PUT,
        f'{WAS_FOLDERS_URL}/{FOLDER_ID}',
        json=FOLDER,
    )
    resp = api.v3.was.folders.edit(FOLDER_ID, new_name)
    assert resp == FOLDER


@responses.activate
def test_search(api):
    '''
    Test was folders search method
    '''
    response = {
        'folders': [FOLDER],
        'pagination': {'total': 1, 'next': 'nextToken'}
    }

    fields = ['unread_count',
              'custom',
              'default_tag',
              'type',
              'name',
              'id']
    filters = {
        'and': [
            {
                'property': 'name',
                'operator': 'eq',
                'value': 'Trash'
            }
        ]
    }

    api_payload = {
        'fields': fields,
        'filter': filters,
        'limit': 2,
        'sort': [{'name': 'desc'}],
    }

    responses.add(
        responses.POST,
        f'{WAS_FOLDERS_URL}/search',
        json=response,
        match=[responses.matchers.json_params_matcher(api_payload)]
    )
    resp = api.v3.was.folders.search(
        fields=fields,
        filter=filters,
        sort=[('name', 'desc')],
        limit=2
    )
    assert isinstance(resp, SearchIterator)

    for ind, folder in enumerate(resp):
        assert folder == response['folders'][ind]

    resp = api.v3.was.folders.search(
        fields=fields,
        filter=filters,
        sort=[('name', 'desc')],
        limit=2,
        return_csv=True
    )
    assert isinstance(resp, CSVChunkIterator)

    resp = api.v3.was.folders.search(
        fields=fields,
        filter=filters,
        sort=[('name', 'desc')],
        limit=2,
        return_resp=True
    )
    assert isinstance(resp, requests.Response)
