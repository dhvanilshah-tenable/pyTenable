'''
Scanner Groups
==============

The following methods allow for interaction into the Tenable.io
:devportal:`scanner-groups <scanner-groups>` API endpoints.

Methods available on ``tio.v3.vm.scanner_groups``:

.. rst-class:: hide-signature
.. autoclass:: ScannerGroupsAPI
    :members:
'''
from typing import Dict, List, Optional
from uuid import UUID

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.vm.scanner_groups.schema import ScannerGroupsBaseSchema


class ScannerGroupsAPI(ExploreBaseEndpoint):
    '''
    This will contain all methods related to scanner groups
    '''

    _path = 'api/v3/scanner-groups'
    _conv_json = True

    def add_scanner(self, group_id: UUID, scanner_id: UUID) -> None:
        '''
        Add a scanner to a scanner group.

        :devportal:`scanner-groups: add-scanner <scanner-groups-add-scanner>`

        Args:
            group_id (UUID):
                The unique identifier of the scanner group.
            scanner_id (UUID):
                The unique identifier of the scanner.

        Returns:
            :obj:`None`:
                Scanner successfully added to the scanner group.

        Examples:
            >>> tio.v3.vm.scanner_groups.add_scanner(1, 1)
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id', 'scanner_id'])
        schema.load(dict(group_id=group_id, scanner_id=scanner_id))
        self._post(f'{group_id}/scanners/{scanner_id}')

    def create(
            self, name: str, group_type: Optional[str] = 'load_balancing'
    ) -> Dict:
        '''
        Create a scanner group.

        :devportal:`scanner-groups: create <scanner-groups-create>`

        Args:
            name (str): The name of the scanner group to create
            group_type (str, optional):
                The type of scanner group to create.  Currently the only
                supported type is "load_balancing"

        Returns:
            :obj:`dict`:
                The scanner group resource record for the created group.

        Example:
            >>> group = tio.v3.vm.scanner_groups.create('Scanner Group')
        '''
        payload = {
            'name': name,
            'type': group_type
        }
        schema = ScannerGroupsBaseSchema(only=['name', 'type'])
        schema.load(payload)
        return self._post(json=payload)

    def delete(self, group_id: UUID) -> None:
        '''
        Deletes a scanner group.

        :devportal:`scanner-groups: delete <scanner-groups-delete>`

        Args:
            group_id (UUID):
                The unique identifier for the scanner group to delete.

        Returns:
            :obj:`None`:
                The scanner group has been successfully deleted.

        Examples:
            >>> tio.v3.vm.scanner_groups.delete(1)
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id'])
        schema.load(dict(group_id=group_id))
        self._delete(f'{group_id}')

    def delete_scanner(self, group_id: UUID, scanner_id: UUID) -> None:
        '''
        Removes a scanner from a scanner group.

        :devportal:`scanner-groups: delete-scanner
         <scanner-groups-delete-scanner>`

        Args:
            group_id (UUID):
                The unique identifier of the scanner group.
            scanner_id (UUID):
                The unique identifier of the scanner to remove from the
                requested scanner group.

        Returns:
            :obj:`None`:
                The scanner was successfully removed from the scanner group.

        Examples:
            >>> tio.v3.vm.scanner_groups.delete_scanner(1, 1)
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id', 'scanner_id'])
        schema.load(dict(group_id=group_id, scanner_id=scanner_id))
        self._delete(f'{group_id}/scanners/{scanner_id}')

    def details(self, group_id: UUID) -> Dict:
        '''
        Retrieves the details about a scanner group.

        :devportal:`scanner-groups: details <scanner-groups-details>`

        Args:
            group_id (UUID): The unique identifier for the scanner group.

        Returns:
            :obj:`dict`:
                The scanner group resource record.

        Examples:
            >>> group = tio.v3.vm.scanner_groups.details(1)
            >>> pprint(group)
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id'])
        schema.load(dict(group_id=group_id))
        return self._get(f'{group_id}')

    def edit(self, group_id: UUID, name: str) -> None:
        '''
        Modifies a scanner group.

        :devportal:`scanner-groups: edit <scanner-groups-edit>`

        Args:
            group_id (UUID): The unique identifier for the scanner group.
            name (str): The new name for the scanner group.

        Returns:
            :obj:`None`:
                The scanner group has been successfully updated.

        Examples:
            >>> tio.v3.vm.scanner_groups.edit(1, 'New Group Name')
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id', 'name'])
        schema.load(dict(group_id=group_id, name=name))
        self._put(f'{group_id}', json={'name': name})

    def search_scanner_groups(self):
        # '''
        # Lists the configured scanner groups.
        #
        # :devportal:`scanner-groups: list <scanner-groups-list>`
        #
        # Returns:
        #     :obj:`list`:
        #         List of scanner group resource records.
        #
        # Examples:
        #     >>> for group in tio.scanner_groups.list():
        #     ...     pprint(group)
        # '''
        # return self._api.get('scanner-groups').json()['scanner_pools']
        raise NotImplementedError('This endpoint is still is development')

    def list_scanners(self, group_id: UUID) -> List:
        '''
        List the scanners within a specific scanner group.

        :devportal:`scanner-groups: list-scanners
        scanner-groups-list-scanners>`

        Args:
            group_id (UUID): The unique identifier of the scanner group.

        Returns:
            :obj:`list`:
                List of scanner resource records associated
                to the scanner group.

        Examples:
            >>> for scanner in tio.scanner_groups.list_scanners(1):
            ...     pprint(scanner)
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id'])
        schema.load(dict(group_id=group_id))
        return self._get(f'{group_id}/scanners')['scanners']

    def list_routes(self, group_id: UUID) -> List:
        '''
        List the hostnames, wildcards, IP addresses,
            and IP address ranges that Tenable.io
             matches against targets in auto-routed scans

        :devportal:`scanner-groups: list-routes <scanner-groups-list-routes>`

        Args:
            group_id (UUID): The unique identifier of the scanner group

        Returns:
            :obj:`list`:
                List of routes associated to the scanner group.

         Examples:
            >>> for scanner in tio.v3.vm.scanner_groups.list_routes(1):
            ...     pprint(scanner)
        '''
        schema = ScannerGroupsBaseSchema(only=['group_id'])
        schema.load(dict(group_id=group_id))
        return self._get(f'{group_id}/routes')

    def edit_routes(self, group_id: UUID, routes: List[str]) -> None:
        '''
        Updates the hostnames, hostname wildcards,
         IP addresses, and IP address ranges
        that Tenable.io matches against targets in auto-routed scans

        :devportal:`scanner-groups: edit-routes <scanner-groups-edit-routes>`

        Args:
            group_id (UUID): The unique identifier of the scanner group
            routes (list): The list of routes for scanner group

        Returns:
            :obj:`None`:
                The scanner group routes has been successfully updated

         Examples:
            >>> tio.v3.vm.scanner_groups.edit_routes(1, ['127.0.0.1'])
        '''
        schema = ScannerGroupsBaseSchema(only=['routes', 'group_id'])
        payload = schema.dump(schema.load(
            dict(routes=routes, group_id=group_id)
        ))
        payload.pop('group_id')
        self._put(f'{group_id}/routes', json=payload)
