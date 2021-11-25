"""
Groups
======

The following methods allow for interaction into the Tenable.io
:devportal:`groups <groups>` API.

Methods available on ``tio.v3.groups``:

.. rst-class:: hide-signature
.. autoclass:: GroupsAPI
    :members:
"""
from typing import Dict, List
from uuid import UUID

from tenable.io.v3.base.endpoints.uw import UWBaseEndpoint


class GroupsAPI(UWBaseEndpoint):

    _path = "api/v3/groups"
    _conv_json = True

    def add_user(self, group_id: UUID, user_id: UUID) -> None:
        """
        Add a user to a user group.

        :devportal:`groups: add-user <groups-add-user>`

        Args:
            group_id:
                The unique identifier of the group to add the user to.
            user_id:
                The unique identifier of the user to add.

        Returns:
            None:
                The user was successfully added to the group.

        Examples:
            >>> tio.v3.groups.add_user('00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000')
        """
        self._post(f"{group_id}/users/{user_id}")

    def create(self, name: str) -> Dict:
        """
        Create a new user group.

        :devportal:`groups: create <groups-create>`

        Args:
            name:
                The name of the group that will be created.

        Returns:
            Dict:
                The group resource record of the newly minted group.

        Examples:
            >>> group = tio.v3.groups.create('Group Name')
        """
        return self._post(json={"name": name})

    def delete(self, id: UUID) -> None:
        """
        Delete a user group.

        :devportal:`groups: delete <groups-delete>`

        Args:
            id: The unique identifier for the group to be deleted.

        Returns:
            None:
                The group was successfully deleted.

        Examples:
            >>> tio.v3.groups.delete('00000000-0000-0000-0000-000000000000')
        """
        self._delete(id)

    def delete_user(self, group_id: UUID, user_id: UUID) -> None:
        """
        Delete a user from a user group.

        :devportal:`groups: delete-user <groups-delete-user>`

        Args:
            group_id:
                The unique identifier for the group to be modified.
            user_id:
                The unique identifier for the user to be removed from the group.

        Returns:
            None:
                The user was successfully removed from the group.

        Examples:
            >>> tio.v3.groups.delete_user('00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000')
        """
        self._delete(f"{group_id}/users/{user_id}")

    def edit(self, id: UUID, name: str) -> Dict:
        """
        Edit a user group.

        :devportal:`groups: edit <groups/edit>`

        Args:
            id:
                The unique identifier for the group to be modified.
            name (str):
                The new name for the group.

        Returns:
            Dict:
                The group resource record.

        Examples:
            >>> tio.v3.groups.edit('00000000-0000-0000-0000-000000000000', 'Updated name')
        """
        return self._put(str(id), json={"name": name})

    def list(self) -> List:
        """
        Lists all of the available user groups.

        :devportal:`groups: list <groups-list>`

        Returns:
            List:
                List of the group resource records

        Examples:
            >>> for group in tio.v3.groups.list():
            ...     pprint(group)
        """
        return self._post("search", json={})["groups"]

    def list_users(self, id: UUID) -> List:
        """
        List the user memberships within a specific user group.

        :devportal:`groups: list-users <groups-list-users>`

        Args:
            id: The unique identifier of the group requested.

        Returns:
            List:
                List of user resource records based on membership to the
                specified group.

        Example:
            >>> for user in tio.v3.groups.list_users('00000000-0000-0000-0000-000000000000'):
            ...     pprint(user)
        """
        return self._get(f"{id}/users")["users"]
