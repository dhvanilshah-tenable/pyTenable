'''
Folders
=======

The following methods allow for interaction into the Tenable.io
:devportal:`Web Application Scanning v3 folders
<was-v2-folders>` API endpoints.

Methods available on ``tio.v3.was.folders``:

.. rst-class:: hide-signature
.. autoclass:: FoldersAPI
    :members:
'''
from typing import Dict, Union
from uuid import UUID

from requests import Response

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.base.iterators.explore_iterator import (CSVChunkIterator,
                                                           SearchIterator)
from tenable.io.v3.was.folders.schema import FolderSchema


class FoldersAPI(ExploreBaseEndpoint):
    _path = 'api/v3/was/folders'
    _conv_json = True
    _schema = FolderSchema()

    def create(self, name: str) -> Dict:
        '''
        Create a folder.

        :devportal:`was folders: create <was-v2-folders-create>`

        Args:
            name (str): The name of the new folder.

        Returns:
            :obj:`dict`: The resource record of the newly created folder.

        Examples:
            >>> folder = tio.v3.was.folders.create('New Folder Name')
        '''
        payload = self._schema.dump(self._schema.load({'name': name}))
        return self._post(json=payload)

    def delete(self, id: UUID) -> None:
        '''
        Delete a folder.

        :devportal:`was folders: delete <was-v2-folders-delete>`

        Args:
            id (UUID): The unique identifier for the folder.

        Returns:
            :obj:`None`

        Examples:
            >>> tio.v3.was.folders.delete('91843ecb-ecb8-48a3-b623-d4682c28c')
        '''
        self._delete(f'{id}')

    def edit(self, id: UUID, name: str) -> Dict:
        '''
        Edit a folder.

        :devportal:`was folders: edit <was-v2-folders-update>`

        Args:
            id (UUID): The unique identifier for the folder.
            name (str): The new name for the folder.

        Returns:
            :obj:`dict`: The resource record of the updated folder.

        Examples:
            >>> tio.v3.was.folders.edit('91843ecb-ecb8-48a3-b623-d4682c2594',
            ...     'Updated Folder Name')
        '''
        payload = self._schema.dump(self._schema.load({'name': name}))
        return self._put(f'{id}', json=payload)

    def search(self, **kwargs) -> Union[CSVChunkIterator,
                                        Response,
                                        SearchIterator]:
        '''
        Search and retrieve the accounts based on supported conditions.
        Args:
            fields (list, optional):
                The list of field names to return from the Tenable API.
                Example:
                    >>> ['field1', 'field2']
            filter (tuple, Dict, optional):
                A nestable filter object detailing how to filter the results
                down to the desired subset.
                Examples:
                    >>> ('or', ('and', ('test', 'oper', '1'),
                    ...                 ('test', 'oper', '2')
                    ...             ),
                    ...     'and', ('test', 'oper', 3)
                    ... )
                    >>> {
                    ...  'or': [{
                    ...      'and': [{
                    ...              'value': '1',
                    ...              'operator': 'oper',
                    ...              'property': '1'
                    ...          },
                    ...          {
                    ...              'value': '2',
                    ...              'operator': 'oper',
                    ...              'property': '2'
                    ...          }
                    ...      ]
                    ...  }],
                    ...  'and': [{
                    ...      'value': '3',
                    ...      'operator': 'oper',
                    ...      'property': 3
                    ...  }]
                    ... }
                As the filters may change and sortable fields may change over
                time, it's highly recommended that you look at the output of
                the :py:meth:`tio.v3.was.folders.filters()`
                endpoint to get more details.
            sort (list[tuple], optional):
                A list of dictionaries describing how to sort the data
                that is to be returned.
                Examples:
                    >>> [('field_name_1', 'asc'),
                    ...      ('field_name_2', 'desc')]
            limit (int, optional):
                Number of objects to be returned in each request.
                Default and max_limit is 200.
            next (str, optional):
                The pagination token to use when requesting the next page of
                results. This token is presented in the previous response.
            return_resp (bool, optional):
                If set to true, will override the default behavior to return
                an iterable and will instead return the results for the
                specific page of data.
            return_csv (bool, optional):
                If set to true, it will return the CSV response or
                iterable (based on return_resp flag). Iterator returns all
                rows in text/csv format for each call with row headers.
        Returns:
            Iterable:
                The iterable that handles the pagination for the job.
            requests.Response:
                If ``return_json`` was set to ``True``, then a response
                object is instead returned instead of an iterable.
        Examples:
            >>> tio.v3.mssp.accounts.search(filter=('type', 'eq',
            ...     'private'), fields=['unread_count', 'name', 'id'],
            ...     limit=2, sort=[('name', 'desc')])
        '''
        iclass = SearchIterator
        if kwargs.get('return_csv', False):
            iclass = CSVChunkIterator
        return super()._search(resource='folders',
                               iterator_cls=iclass,
                               sort_type=self._sort_type.default,
                               api_path=f'{self._path}/search',
                               **kwargs
                               )
