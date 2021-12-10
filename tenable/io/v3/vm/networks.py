'''
Networks
========

The following methods allow for interaction into the Tenable.io
:devportal:`networks <networks>` API endpoints.

Methods available on ``tio.v3.vm.networks``:

.. rst-class:: hide-signature
.. autoclass:: NetworksAPI
    :members:
'''
from typing import Dict, List, Union

from tenable.errors import UnexpectedValueError
from tenable.io.base import TIOEndpoint, TIOIterator


class NetworksIterator(TIOIterator):
    '''
    The networks iterator provides a scalable way to work through networks
    result sets of any size.  The iterator will walk through each page
    of data, returning one record at a time.  If it reaches the end of a
    page of records, then it will request the next page of information and
    then continue to return records from the next page (and the next, and the
    next) until the counter reaches the total number of records that the API
    has reported.

    Attributes:
        count (int): The current number of records that have been returned
        page (list):
            The current page of data being walked through.  pages will be
            cycled through as the iterator requests more information from the
            API.
        page_count (int): The number of record returned from the current page.
        total (int):
            The total number of records that exist for the current request.
    '''
    pass


class NetworksAPI(TIOEndpoint):
    '''
    This will contain all methods related to networks
    '''

    def create(self,
               name: str,
               description: str = None,
               assets_ttl_days: int = None
               ) -> Dict:
        '''
        Creates a new network within Tenable.io

        :devportal:`networks: create <networks-create>`

        Args:
            name: The name of the new network.
            description (optional): Description of the network.
            assets_ttl_days (optional):
                The number of days to wait before assets age out.
                Assets will be permanently deleted if they are not seen on
                a scan within the specified number of days.
                Minimum value: 90
                Maximum value: 365

        Returns:
            :obj:`dict`:
                The resource record of the newly created network.

        Examples:
            >>> nw = tio.v3.vm.networks.create('Example')
        '''
        if not description:
            description = ''

        return self._api.post('networks', json={
            'name': name,
            'description': description,
            'assets_ttl_days': assets_ttl_days
        }).json()

    def delete(self, network_id: str) -> None:
        '''
        Deletes the specified network.

        :devportal:`networks: delete <networks-delete>`

        Args:
            network_id: The UUID of the network to remove.

        Examples:
            >>> tio.v3.vm.networks.delete(
                    '00000000-0000-0000-0000-000000000000'
                )
        '''
        self._api.delete(f'networks/{network_id}')

    def details(self, network_id: str) -> Dict:
        '''
        Retrieves the details of the specified network.

        :devportal:`networks: details <networks-details>`

        Args:
            network_id : The UUID of the network.

        Examples:
            >>> nw = tio.v3.vm.networks.details(
                    '00000000-0000-0000-0000-000000000000'
                )
        '''
        return self._get(f'networks/{network_id}')

    def edit(self,
             network_id: str,
             name: str,
             description=None,
             assets_ttl_days=None
             ) -> Dict:
        '''
        Updates the specified network resource.

        :devportal:`networks: update <networks-update>`

        Args:
            network_id: The UUID of the network resource to update.
            name: The new name of the network resource.
            description (str, optional):
                The new description of the network resource.
            assets_ttl_days (int, optional):
                The number of days to wait before assets age out.
                Assets will be permanently deleted if they are not seen on a
                scan within the specified number of days.
                Minimum value: 90
                Maximum value: 365

        Returns:
            :obj:`dict`:
                The updates network resource.

        Examples:
            >>> nw = tio.v3.vm.networks.edit(
                    '00000000-0000-0000-0000-000000000000',
                    'Updated Network', 'Updated Description', 180
                )
        '''
        if not description:
            description = ''

        return self._put(f'networks/{network_id}',
                         json={
                             'name': name,
                             'description': description,
                             'assets_ttl_days': assets_ttl_days
                         }
                         )

    def assign_scanners(self,
                        network_id: str,
                        *scanner_uuids: Union[str, List]
                        ) -> None:
        '''
        Assigns one or many scanners to a network.

        :devportal:`networks: assign-scanner <networks-assign-scanner>`
        :devportal:`networks: bulk-assign-scanner
            <networks-assign-scanner-bulk>`

        Args:
            network_id: The UUID of the network.
            *scanner_uuids: Scanner UUID(s) to assign to the network.

        Examples:
            Assign a single scanner:

            >>> tio.v3.vm.networks,assign_scanners(
            ...     '00000000-0000-0000-0000-000000000000', # Network UUID
            ...     '00000000-0000-0000-0000-000000000000') # Scanner UUID

            Assign multiple scanners:

            >>> tio.v3.vm.networks,assign_scanners(
            ...     '00000000-0000-0000-0000-000000000000', # Network UUID
            ...     '00000000-0000-0000-0000-000000000000', # Scanner1 UUID
            ...     '00000000-0000-0000-0000-000000000000') # Scanner2 UUID
        '''
        if len(scanner_uuids) == 1:
            self._post(f'networks/{network_id}/scanners/{scanner_uuids[0]}')
        elif len(scanner_uuids) > 1:
            self._post(f'networks/{network_id}/scanners',
                       json={'scanner_uuids': [id for id in scanner_uuids]}
                       )
        else:
            raise UnexpectedValueError('No scanner_uuids were supplied.')

    def list_scanners(self, network_id: str) -> List:
        '''
        Retrieves the list of scanners associated to a given network.

        :devportal:`networks: list-scanners <networks-list-scanners>`

        Args:
            network_id (str): The UUID of the network.

        Returns:
            :obj:`list`:
                List of scanner resources associated to this network.

        Examples:
            >>> network = '00000000-0000-0000-0000-000000000000'
            >>> for scanner in tio.v3.vm.networks.list_scanners(network):
            ...     pprint(scanner)
        '''
        return self._get(f'networks/{network_id}/scanners')['scanners']

    def unassigned_scanners(self, network_id: str) -> List:
        '''
        Retrieves the list of scanners that are currently unassigned to the
        given network.  This will include scanners and scanner groups that
        are currently assigned to the default network.

        :devportal:`networks: list-assignable-scanners
            <networks-list-assignable-scanners>`

        Args:
            id: The UUID of the network.

        Returns:
            :obj:`list`:
                The list of unassigned scanner resources

        Examples:
            >>> network = '00000000-0000-0000-0000-000000000000'
            >>> for scanner in tio.v3.vm.networks.unassigned_scanners(network):
            ...     pprint(scanner)
        '''
        return self._get(
            f'networks/{network_id}/assignable-scanners'
        )['scanners']

    def search(self, *filters, **kw):
        '''
        Get the listing of configured networks from Tenable.io.

        :devportal:`networks: list <networks-list>`

        Args:
            *filters (tuple, optional):
                Filters are tuples in the form of
                ('NAME', 'OPERATOR', 'VALUE'). Multiple filters can be used
                to filter down the data being returned from the API.

                Examples:
                    - ``('name', 'eq', 'example')``

                As the filters may change and sortable fields may change over
                time, it's highly recommended that you look at the output of
                the :py:meth:`tio.v3.vm.networks.network_filters()
                <FiltersAPI.networks_filters>` endpoint to get more details.
            filter_type (str, optional):
                The filter_type operator determines how the filters are
                combined together. `and` will inform the API that all of the
                filter conditions must be met for an access group to be
                returned, whereas `or` would mean that if any of the
                conditions are met the access group record will be returned.
            include_deleted (bool, optional):
                Indicates whether deleted network objects should be included in
                the response. If left unspecified, the default is `False`.
            limit (int, optional):
                The number of records to retrieve.  Default is 50
            offset (int, optional):
                The starting record to retrieve.  Default is 0.
            sort (tuple, optional):
                A tuple of tuples identifying the the field and sort order of
                the field.
            wildcard (str, optional):
                A str to pattern match against all available fields returned
            wildcard_fields (list, optional):
                A list of fields to optionally restrict the wild-card matching
                to.

        Returns:
            :obj:`NetworksIterator`:
                An iterator that handles the page management of the requested
                records.

        Examples:
            Getting the listing of all agents:

            >>> for nw in tio.v3.vm.networks.list():
            ...     pprint(nw)

            Retrieving all of the windows agents:

            >>> for nw in tio.access_groups.list(('name', 'match', 'win')):
            ...     pprint(nw)
        '''
        return NotImplementedError("Search method will be implemented later")

    def network_asset_count(self, network_id: str, num_days: int) -> Dict:
        '''
        get the total number of assets in the network along with the number
        of assets that have not been seen for the specified number of days.

        :devportal:`networks: network_asset_count
            <networks-asset-count-details>`

        Args:
            network_id: The UUID of the network.
            num_days: count of assets that have not been seen for the
            specified number of days

        Returns:
            :obj:`dict`:
                Returns the total number of assets in the network along with
                the number of assets that have not been seen for the
                specified number of days.

        Examples:
            >>> network = '00000000-0000-0000-0000-000000000000'
            >>> count = tio.v3.vm.networks.network_asset_count(network, 180)
        '''
        return self._get(
            f'networks/{network_id}/counts/assets-not-seen-in/{num_days}'
        )
