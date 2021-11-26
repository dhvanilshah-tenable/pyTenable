"""
Target Groups
=============

The following methods allow for interaction into the Tenable.io
:devportal:`target_groups <target-groups>` API endpoints.

Methods available on ``tio.target_groups``:

.. rst-class:: hide-signature
.. autoclass:: TargetGroupsAPI
    :members:
"""
from typing import List, Dict

from tenable.io.v3.base.endpoints.export import UWBaseEndpoint
from tenable.io.v3.vm.schema import TargetGroupsSchema
from tenable.utils import dict_merge


class TargetGroupsAPI(UWBaseEndpoint):
    _path = "target-groups"
    _conv_json = True

    def create(self, name: str, members: List, **kw) -> Dict:
        """
        Create a target-group.

        :devportal:`target-groups: create <target-groups-create>`

        Args:
            name (str): The name of the target group
            members (list):
                The members of the target group.  FQDNs, CIDRs, IPRanges, and
                individual IPs are supported.
            acls (list, optional):
                A list of ACLs defining how the asset list can be used.  For
                further information on how the ACL dictionaries should be
                written, please refer to the API documentation.

        Returns:
            Dict:
                The resource record of the newly created target group.

        Examples:
            >>> tg = tio.v3.vm.target_groups.create('Example', ['192.168.0.0/24'])
        """
        schema = TargetGroupsSchema()
        if not members:
            members = []
        members = ",".join(members)
        payload = schema.dump(schema.load({"name": name, "members": members, **kw}))
        return self._post(json=payload)

    def delete(self, id: int) -> None:
        """
        Delete a target group.

        :devportal:`target-groups: delete <target-groups-delete>`

        Args:
            id (int): The unique identifier for the target group.

        Returns:
            None:
                The target group was successfully deleted.

        Examples:
            >>> tio.v3.vm.target_groups.delete(1)
        """
        self._delete(f'{id}')

    def details(self, id: int) -> Dict:
        """
        Retrieve the details of a target group.

        :devportal:`target-groups: details <target-groups-details>`

        Args:
            id (int): The unique identifier for the target group.

        Returns:
            Dict:
                The resource record for the target group.

        Examples:
            >>> tg = tio.v3.vm.target_groups.details(1)
        """
        return self._get(f'{id}')

    def edit(self, id: int, **kw) -> Dict:
        """
        Edit an existing target group.

        :devportal:`target-groups: edit <target-groups-edit>`

        Args:
            id (int): The unique identifier for the target group.
            name (str, optional): The name of the target group.
            members (list, optional):
                The members of the target group.  FQDNs, CIDRs, IPRanges, and
                individual IPs are supported.  NOTE: modifying the member list
                is atomic and not additive.  All previous members that are
                desired to be kept within the member list much also be included.
            acls (list, optional):
                A list of ACLs defining how the asset list can be used.  For
                further information on how the ACL dictionaries should be
                written, please refer to the API documentation.  NOTE: modifying
                ACLs is atomic and not additive.  Please provide the complete
                list of ACLs that this asset group will need.

        Returns:
            Dict:
                The modified target group resource record.

        Examples:
            >>> tio.v3.vm.target_groups.edit(1, name='Updated TG Name')
        """
        # We need to get the current asset group and then merge in the modified
        # data.  We will store the information in the same variable as the
        # modified information was built into.
        schema = TargetGroupsSchema(only=("name", "members", "acls"))
        payload = schema.load(kw)
        craw = schema.dump(self.details(id))
        payload = dict_merge(craw, payload)
        return self._put(f'{id}', json=payload)

    def list(self) -> List:
        """
        Retrieve the list of target groups configured.

        :devportal:`target-groups: list <target-groups-list>`

        Returns:
            List:
                Listing of target group resource records.

        Examples:
            >>> for tg in tio.v3.vm.target_groups.list():
            ...     pprint(tg)
        """
        raise NotImplementedError('This method will be updated once Permissions API is migrated to v3')
