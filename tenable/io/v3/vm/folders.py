'''
Folders
=======

The following methods allow for interaction into the Tenable.io
:devportal:`folders <folders>` API endpoints.

Methods available on ``tio.folders``:

.. rst-class:: hide-signature
.. autoclass:: FoldersAPI
    :members:
'''
from typing import List

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class FoldersAPI(ExploreBaseEndpoint):

    _path = 'api/v3/folders'
    _conv_json = True

    def create(self, name: str) -> int:
        '''
        Create a folder.

        :devportal:`folders: create <folders-create>`

        Args:
            name:
                The name of the new folder.

        Returns:
            :obj:`int`:
                The new folder id.

        Examples:
            >>> folder = tio.v3.vm.folders.create('New Folder Name')
        '''
        return self._post(json={'name': name})['id']

    def delete(self, id: int) -> None:
        '''
        Delete a folder.

        :devportal:`folders: delete <folders-delete>`

        Args:
            id: The unique identifier for the folder.

        Returns:
            :obj:`None`

        Examples:
            >>> tio.v3.vm.folders.delete(1)
        '''
        self._delete(f'{id}')

    def edit(self, id: int, name: str) -> None:
        '''
        Edit a folder.

        :devportal:`folders: edit <folders-edit>`

        Args:
            id: The unique identifier for the folder.
            name: The new name for the folder.

        Returns:
            :obj:`None`:
                The folder was successfully renamed.

        Examples:
            >>> tio.v3.vm.folders.edit(1, 'Updated Folder Name')
        '''
        self._put(f'{id}', json={'name': name})

    def list(self) -> List:
        '''
        Lists the available folders.

        :devportal:`folders: list <folders-list>`

        Returns:
            :obj:`list`:
                List of folder resource records.

        Examples:
            >>> for folder in tio.v3.vm.folders.list():
            ...     pprint(folder)
        '''
        return self._get()['folders']
