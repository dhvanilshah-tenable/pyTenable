'''
Assets
======

The following methods allow for interaction into the Tenable.io
:devportal:`assets <assets>` API endpoints.

Methods available on ``tio.v3.assets``:

.. rst-class:: hide-signature
.. autoclass:: AssetsAPI
    :members:
'''
from typing import Dict, List, Tuple, Union
from uuid import UUID

from typing_extensions import Literal

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.base.iterators.search_iterator import SearchIterator
from tenable.io.v3.base.schema.explore.filters import FilterSchema
from tenable.io.v3.base.schema.explore.search import SearchSchema
from tenable.io.v3.base.schema.explore.utils import generate_sort_data

from .schema import AssignTagsAssetSchema, ImportAssetSchema, MoveAssetSchema


class AssetSearchIterator(SearchIterator):
    '''
    asset search iterator
    '''
    pass


class AssetsAPI(ExploreBaseEndpoint):
    '''
    This will contain all methods related to Assets
    '''
    _path = 'api/v3/assets'
    _conv_json = True

    def search_assets(self, *filters, **kw) -> AssetSearchIterator:
        '''
        Retrieves the assets.

        Requires -
            fields (list): ['field1', 'field2']
                    -> fields is not supported by the search_assets api
            filter (tuple): ('field_name', 'operator', 'value')
                    -- ('and', ('test', 'oper', '1'), ('test', 'oper', '2'))
            sort List(tuple): 'sort': [
                        {'last_observed': 'desc'}
                    ]
            limit (int): (10)
            next (str): ('adfj3u4j34u9j48wi3j5w84jt5') -> next token

        Returns:
            Iterable:
                The iterable that handles the pagination and potentially
                async requests for the job.

        '''

        filter_schema = FilterSchema()
        search_schema = SearchSchema()
        query = filter_schema.dump(filter_schema.load(filters[0]))
        sort_data = generate_sort_data(kw, is_with_prop=False)
        kw.update({'filter': query,
                   'sort': sort_data})
        payload = search_schema.dump(search_schema.load(kw))
        return AssetSearchIterator(
            api=self,
            _limit=payload['limit'],
            _path='search',
            _resource='assets',
            _payload=payload
        )

    def delete(self, uuid: UUID) -> None:
        '''
        Deletes the asset.

        :devportal:`assets: asset-delete <asset-delete>`

        Args:
            uuid (str): The unique identifier for the asset.

        Returns:
            None:

        Examples:
            >>> asset_id = '00000000-0000-0000-0000-000000000000'
            >>> tio.v3.delete(asset_id)
        '''
        return self._delete(uuid)

    def details(self, uuid: UUID) -> Dict:
        '''
        Retrieves the details about a specific asset.

        :devportal:`assets: asset-info <assets-asset-info>`

        Args:
            uuid:
                The UUID (unique identifier) for the asset.

        Returns:
            Dict:
                Asset resource definition.

        Examples:
            >>> asset = tio.v3.assets.details(
            ...     '00000000-0000-0000-0000-000000000000')
        '''
        return self._get(f'{uuid}')

    def assign_tags(
        self, action: Literal['add', 'remove'],
            assets: List[UUID], tags: List[UUID]
    ) -> Dict:
        '''
        Add/remove tags for asset(s).

        :devportal:`tags: assign-asset-tags <tags-assign-asset-tags>`

        Args:
            action:
                Specifies whether to add or remove tags.
                 Valid values: add, remove.
            assets:
                An array of asset UUIDs.
            tags:
                An array of tag value UUIDs.

        Returns:
            Obj:Dict:
                The job Resource record.

        Examples:
            >>> asset = tio.v3.assets.assign_tags(
            ...     'add', ['00000000-0000-0000-0000-000000000000'],
            ...     ['00000000-0000-0000-0000-000000000000'])
        '''
        # pylint: disable=unused-variable
        schema = AssignTagsAssetSchema()
        payload = schema.dump(
            schema.load({'action': action, 'assets': assets, 'tags': tags})
        )
        print(payload)
        # return self._api.post('tags/assets/assignments', json=payload).json()
        raise NotImplementedError('Not implemented yet as it depends on tags')

    def tags(self, uuid: UUID) -> Dict:
        '''
        Retrieves the details about a specific asset.

        :devportal:`tags: asset-tags <tags-list-asset-tags>`

        Args:
            uuid:
                The UUID (unique identifier) for the asset.

        Returns:
            Dict:
                Asset resource definition.

        Examples:
            >>> asset = tio.v3.assets.tags(
            ...     '00000000-0000-0000-0000-000000000000')
        '''
        raise NotImplementedError('Not implemented yet as it depends on tags')

    def asset_import(self, source: str, *assets: Dict) -> str:
        '''
        Imports asset information into Tenable.io from an external source.

        :devportal:`assets: import <assets-import>`

        Imports a list of asset definition dictionaries.
        Each asset record must
        contain at least one of the following attributes: ``fqdn``, ``ipv4``,
        ``netbios_name``, ``mac_address``.  Each record may also contain
        additional properties.

        Args:
            *assets:
                One or more asset definition dictionaries
            source:
                An identifier to be used to upload the assets.

        Returns:
            str:
                The job UUID.

        Examples:
            import single asset:

            >>> tio.v3.assets.asset_import('example_source', {
            ...     'fqdn': ['example.py.test'],
            ...     'ipv4': ['192.168.254.1'],
            ...     'netbios_name': 'example',
            ...     'mac_address': ['00:00:00:00:00:00']
            ... })

            import multiple asset:

            >>> tio.v3.assets.asset_import('multiple_asset_example_source',
            ...     {
            ...         'fqdn': ['example_one.py.test'],
            ...         'ipv4': ['192.168.1.1'],
            ...         'netbios_name': 'example_one',
            ...         'mac_address': ['00:00:00:00:00:00']
            ...     },{
            ...         'fqdn': ['example_two.py.test'],
            ...         'ipv4': ['192.168.255.1'],
            ...         'netbios_name': 'example_two',
            ...         'mac_address': ['00:00:00:00:00:00']
            ...     })
        '''
        # We will likely want to perform some more stringent checking of the
        # asset resources that are being defined, however a simple type check
        # should suffice for now.
        schema = ImportAssetSchema()
        payload = schema.dump(schema.load({'assets': assets,
                                           'source': source}))
        return self._post('import', json=payload)['asset_import_job_uuid']

    def list_import_jobs(self) -> List:
        '''
        Returns a list of asset import jobs.

        :devportal:`assets: list-import-jobs <assets-list-import-jobs>`

        Returns:
            List:
                List of job records.

        Examples:
            >>> for job in tio.v3.assets.list_import_jobs():
            ...     pprint(job)
        '''
        return self._get('import/jobs')['asset_import_jobs']

    def import_job_details(self, uuid: UUID) -> Dict:
        '''
        Returns the details about a specific asset import job.

        :devportal:`assets: import-job-info <assets-import-job-info>`

        uuid:
            The UUID (unique identifier) for the job.

        Returns:
            Dict:
                The job Resource record.

        Examples:
            >>> job = tio.v3.assets.import_job_details(
            ...     '00000000-0000-0000-0000-000000000000')
            >>> pprint(job)
        '''
        return self._get(f'import/jobs/{uuid}')

    def move_assets(
            self, source: UUID, destination: UUID, targets: List[str]
    ) -> int:
        '''
        Moves assets from the specified network to another network.

        :devportal:`assets: move-assets <assets-bulk-move>`

        source:
            The UUID of the network currently associated with the assets.
        destination:
            The UUID of the network to associate with the specified assets.
        targets:
            The IPv4 addresses of the assets to move.

        Returns:
            int:
                Returns the number of moved assets.

        Examples:
            >>> asset = tio.v3.assets.move_assets(
            '00000000-0000-0000-0000-000000000000',
            ...         '10000000-0000-0000-0000-000000000001', ['127.0.0.1'])
            >>> pprint(asset)
        '''
        schema = MoveAssetSchema()
        payload = schema.dump(
            schema.load(
                {'source': source,
                 'destination': destination, 'targets': targets}
            )
        )

        return self._patch(json=payload)['response']['data']['asset_count']

    def bulk_delete(
            self, *filters: Tuple[str], filter_type: str = None
    ) -> Dict:
        '''
        Deletes the specified assets.

        :devportal:`assets: bulk_delete <assets-bulk-delete>`

        Args:
             *filters (tuple):
                A defined filter tuple consisting of the name, operator, and
                value.  Example: ``('host.hostname', 'match', 'asset.com')``.
            filter_type (str, optional):
                If multiple filters are defined, the filter_type toggles the
                behavior as to how these filters are used.  Either all of the
                filters have to match (``AND``) or any of the filters have to
                match (``OR``).  If not specified, the default behavior is to
                assume filter_type is ``AND``.

        Returns:
            Dict:
                Returns the number of deleted assets.

        Examples:
            >>> asset = tio.v3.assets.bulk_delete(
            ...     ('host.hostname', 'match', 'asset.com'), filter_type='or')
            >>> pprint(asset)
        '''
        # payload = {}

        # # run the rules through the filter parser...
        # filter_type = self._check('filter_type', filter_type, str,
        #     choices=['and', 'or'], default='and', case='lower')
        # parsed = self._parse_filters(
        #     filters, self._filters.workbench_asset_filters(),
        #     rtype='assets')['asset']

        # payload['query'] = {filter_type: parsed}

        # return self._post('api/v2/assets/bulk-jobs/delete', json=payload)

        # schema = SomeSchema()
        # payload = schema.dump(schema.load(filter))
        # return self._delete(json=filter)

        raise NotImplementedError(
            'Not implemented yet as it depends on search functionality'
        )

    def update_acr(self, *assets: Union[Dict, List[Dict]]):
        raise NotImplementedError('API has not been implemented yet')

    def search_host(self, filter: Dict):
        raise NotImplementedError('search API has not been implemented yet')
