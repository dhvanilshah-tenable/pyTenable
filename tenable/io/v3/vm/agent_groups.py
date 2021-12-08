'''
Agent Groups
============

The following methods allow for interaction into the Tenable.io
:devportal:`agent groups <agent-groups>` API endpoints.

Methods available on ``tio.v3.vm.agent_groups``:

.. rst-class:: hide-signature
.. autoclass:: AgentGroupsAPI
    :members:
'''
from typing import Dict, Union

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class AgentGroupsAPI(ExploreBaseEndpoint):
    _path: str = f'api/v3/agent-groups'
    _conv_json: bool = True

    def add_agent(self, group_id: int, *agent_ids: int) -> Union[None, Dict]:
        '''
        Adds an agent or multiple agents to the agent group specified.

        :devportal:`agent-groups: add-agent <agent-groups-add-agent>`

        Args:
            group_id (int): The id of the group
            agent_ids (int): The id of the agent

        Returns:
            :obj:`dict` or :obj:`None`:
                If adding a singular agent, a :obj:`None` response will be
                returned.  If adding multiple agents, a :obj:`dict` response
                will be returned with a task record.

        Examples:
            Adding a singular agent:

            >>> tio.v3.vm.agent_groups.add_agent(1, 1)

            Adding multiple agents:

            >>> tio.v3.vm.agent_groups.add_agent(1, 1, 2, 3)
        '''

        if len(agent_ids) <= 1:
            # if there is only 1 agent id, we will perform a singular add.
            self._put(f'{group_id}/agents/{agent_ids[0]}')
        else:
            # If there are many agent_ids, then we will want to perform a
            # bulk operation.
            return self._post(
                f'{group_id}/agents/_bulk/add',
                json={'items': [i for i in agent_ids]}
            )

    def configure(self, group_id: int, name: str) -> Dict:
        '''
        Renames an existing agent group.

        :devportal:`agent-groups: configure <agent-groups-configure>`

        Args:
            group_id (int): The id of the group
            name (str): The new name for the agent group

        Returns:
            :obj:`dict`

        Examples:
            >>> tio.v3.vm.agent_groups.configure(1, 'New Name')
        '''
        return self._put(f'{group_id}', json={'name': name})

    def create(self, name: str) -> Dict:
        '''
        Creates a new agent group.

        :devportal:`agent-groups: create <agent-groups-create>`

        Args:
            name (str): The name of the agent group

        Returns:
            :obj:`dict`:
                The dictionary object representing the newly minted agent group

        Examples:
            >>> group = tio.v3.vm.agent_groups.create('New Agent Group')
        '''
        return self._post(f'', json={'name': name})

    def delete(self, group_id: int) -> None:
        '''
        Delete an agent group.

        :devportal:`agent-groups: delete <agent-groups-delete>`

        Args:
            group_id (int): The id of the agent group to delete

        Returns:
            :obj:`None`

        Examples:
            >>> tio.v3.vm.agent_groups.delete(1)
        '''
        self._delete(f'{group_id}')

    def delete_agent(self, group_id: int, *agent_ids: int)\
            -> Union[None, Dict]:
        '''
        Delete one or many agents from an agent group.

        :devportal:`agent-groups: delete-agent <agent-groups-delete-agent>`

        Args:
            group_id (int): The id of the agent group to remove the agent from
            *agent_ids (int): The id of the agent to be removed

        Returns:
            :obj:`dict` or :obj:`None`:
                If deleting a singular agent, a :obj:`None` response will be
                returned.  If deleting multiple agents, a :obj:`dict` response
                will be returned with a Job resource record.

        Examples:
            Delete a singular agent from an agent group:

            >>> tio.v3.vm.agent_groups.delete_agent(1, 1)

            Delete multiple agents from an agent group:

            >>> tio.v3.vm.agent_groups.delete_agent(1, 1, 2, 3)
        '''
        if len(agent_ids) <= 1:
            # if only a singular agent_id was passed, then we will want to
            self._delete(f'{group_id}/agents/{agent_ids[0]}')
        else:
            # if multiple agent ids were requested to be deleted, then we will
            # call the bulk deletion API.
            return self._post(
                f'{group_id}/agents/_bulk/remove',
                json={'items': [i for i in agent_ids]}
            )

    def details(self):
        NotImplemented('This method will be updated later'
                       'once the filter API will develop')

    def search(self):
        NotImplemented('Search and Filter functionality '
                       'will be updated later.')

    def task_status(self, group_id: int, task_uuid: str) -> Dict:
        '''
        Retrieves the current status of a bulk task.

        :devportal:`bulk-operations: bulk-agent-group-status
        <bulk-task-agent-group-status>`

        Args:
            group_id (int): The id of the group
            task_uuid (str): The id of the task

        Returns:
            :obj:`dict`:
                Task resource

        Examples:
            >>> item = tio.v3.vm.agent_groups.add_agent(1, 21, 22, 23)
            >>> task = tio.v3.vm.agent_groups.task_status(item['task_uuid'])
            >>> pprint(task)
        '''
        return self._get(f'{group_id}/agents/_bulk/{task_uuid}')
