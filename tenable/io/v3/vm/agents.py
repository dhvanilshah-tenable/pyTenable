'''
Agents
======

The following methods allow for interaction into the Tenable.io
:devportal:`agents <agents>` API endpoints.

Methods available on ``tio.v3.vm.agents``:

.. rst-class:: hide-signature
.. autoclass:: AgentsAPI
    :members:
'''
from typing import Dict, Union

from tenable.io.base import TIOIterator
from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class AgentsIterator(TIOIterator):
    '''
    The agents iterator provides a scalable way to work through agent result
    sets of any size.  The iterator will walk through each page of data,
    returning one record at a time.  If it reaches the end of a page of
    records, then it will request the next page of information and then
    continue to return records from the next page (and the next, and the next)
    until the counter reaches the total number of records that the API has
    reported.

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


class AgentsAPI(ExploreBaseEndpoint):
    _path: str = 'api/v3/agents'
    _conv_json: bool = True

    def details(self, agent_id: int) -> Dict:
        '''
        Retrieves the details of an agent.

        :devportal:`agents: get <agents-get>`

        Args:
            agent_id (int):
                The identifier of the agent.

        Returns:
            :obj:`dict`:
                The agent dictionary record.

        Examples:
            >>> agent = tio.v3.vm.agents.details(1)
            >>> pprint(agent)
        '''
        return self._get(f'{agent_id}')

    def list_agents_from_group(self, agent_group_id: int) -> Dict:
        '''
        Retrive the list of agents for the specified agent group.

        :devportal:`agent: get <agent-group-list-agents>`

        Args:
            agent_group_id (int) : The id of the agent group

        Returns:
            :obj:`dict`:
                The agent groups dictionary of all the agents.

        Examples:
            >>> agent_from_group = tio.v3.vm.agents.list_agents_from_groups(1)
            >>> print(agent_from_group)
        '''
        self._path: str = self._path.replace('agents', 'agent-groups')
        return self._get(f'{agent_group_id}/agents/')

    def task_status(self, task_uuid: str) -> Dict:
        '''
        Retrieves the current status of the task requested.

        :devportal:`bulk-operations: bulk-agent-status
        <bulk-task-agent-status>`

        Args:
            task_uuid (str): The id of the agent

        Returns:
            :obj:`dict`:
                Task resource

        Examples:
            >>> item = tio..v3.vm.agents.unlink(21, 22, 23)
            >>> task = tio.v3.vm.agent.task_status(item['task_uuid'])
            >>> pprint(task)
        '''
        return self._get(f'_bulk/{task_uuid}')

    def search(self):
        NotImplemented('This method will be implemented later.')

    def unlink(self, *agent_ids: int) -> Union[Dict, None]:
        '''
        Unlink one or multiple agents from the Tenable.io instance.

        :devportal:`agents: delete <agents-delete>`

        Args:
            *agent_ids (int):
                The ID of the agent to delete

        Returns:
            :obj:`dict` or :obj:`None`:
                If unlinking a singular agent, a :obj:`None` response will be
                returned.  If unlinking multiple agents, a :obj:`dict` response
                will be returned with a task record.

        Examples:
            Unlink a singular agent:

            >>> tio.v3.vm.agents.unlink(1)

            Unlink many agents:

            >>> tio.v3.vm.agents.unlink(1, 2, 3)
        '''

        if len(agent_ids) <= 1:
            # as only a singular agent_id was sent over, we can call the delete
            # API
            self._delete(f'{agent_ids[0]}')
        else:
            return self._post(
                '_bulk/unlink',
                json={'items': [i for i in agent_ids]}
            )
