'''
Permissions
===========

The following methods allow for interaction into the Tenable.io
:devportal`permissions <permissions-1>` API endpoints.

Methods available on ``tio.v3.vm.permissions``:

.. rst-class:: hide-signature
.. autoclass:: PermissionsAPI
    :members:
'''
from typing import List

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.vm.permissions.schema import PermissionSchema


class PermissionsAPI(ExploreBaseEndpoint):
    '''
    This will contain all methods related to Permissions API
    '''

    _path = "api/v3/permissions"
    _conv_json = True
    _schema = PermissionSchema()

    def change(self, otype: str, id: int, *acls: List) -> None:
        '''
        Modify the permission of a specific object.

        :devportal:`permissions: change <permissions-change>`

        Args:
            otype:
                The type of object to change.
            id:
                The unique identifier of the object.
            *acls:
                ACL dictionaries inform Tenable.io how to handle permissions of
                the various objects within Tenable.io.  Please refer to the
                `permissions documentation`_ for more details.

        Returns:
            :obj:`None`:
                The object permissions were successfully changed.

        .. _permissions documentation:
            https://developer.tenable.com/docs/permissions

        Examples:
            >>> tio.v3.vm.permissions.change(otype, id, acls)
        '''
        # # Check to make sure all of the ACLs are dictionaries.
        # for item in acls:
        #     self._check('acl', item, dict)

        # Make the API call.
        payload = self._schema.dump(self._schema.load({'acls': acls}))
        self._put(f'{otype}/{id}', json=payload)

    def list(self, otype: str, id: int) -> List:
        '''
        List the permissions of a specific object.

        :devportal:`permissions: list <permissions-list>`

        Args:
            otype:
                The type of object being queried.
            id:
                The unique identifier of the object.

        Returns:
            :obj:`list`:
                The permission recourse record listings for the
                specified object.

        Examples:
            >>> tio.v3.vm.permissions.list(otype, id)
        '''
        return self._get(f'{otype}/{id}')['acls']

    def search(self):
        '''
        Search method for Permissions API

        Args

        Returns
        '''
        raise NotImplementedError("Search method will be implemented later")
