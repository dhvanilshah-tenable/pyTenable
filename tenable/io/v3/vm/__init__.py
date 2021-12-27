'''
Vulnerability Management
========================

The following API's are available for interaction under
Vulnerability Management platform.

Methods available on ``tio.v3.vm``:


.. rst-class:: hide-signature
.. autoclass:: VulnerabilityManagement
    :members:

.. toctree::
    :hidden:
    :glob:

    agent_config
    agent_groups
    agents
    files
    folders
    networks
    permissions
    plugins
    scanners
    scanner_groups
'''
from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.vm.agent_config.api import AgentConfigAPI
from tenable.io.v3.vm.agent_groups.api import AgentGroupsAPI
from tenable.io.v3.vm.agents.api import AgentsAPI
from tenable.io.v3.vm.files.api import FileAPI
from tenable.io.v3.vm.folders.api import FoldersAPI
from tenable.io.v3.vm.networks.api import NetworksAPI
from tenable.io.v3.vm.permissions.api import PermissionsAPI
from tenable.io.v3.vm.plugins.api import PluginsAPI
from tenable.io.v3.vm.scanner_groups.api import ScannerGroupsAPI
from tenable.io.v3.vm.scanners.api import ScannersAPI


class VulnerabilityManagement(ExploreBaseEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources
    under Vulnerability Management
    i.e assets, agents, scanners etc.
    '''

    @property
    def agent_config(self):
        '''
        The interface object for the
        :doc:`Agent Config APIs <agent_config>`.
        '''
        return AgentConfigAPI(self._api)

    @property
    def agent_groups(self):
        '''
        The interface object for the
        :doc:`Tenable.io Agent Groups APIs <agent_groups>`.
        '''
        return AgentGroupsAPI(self)

    @property
    def agents(self):
        '''
        The interface object for the
        :doc:`Tenable.io Agents APIs <agents>`.
        '''
        return AgentsAPI(self)

    @property
    def files(self):
        '''
        The interface object for the
        :doc:`Files API <files>`
        '''
        return FileAPI(self._api)

    @property
    def folders(self):
        '''
        The interface object for the
        :doc:`Folders API <folders>`
        '''
        return FoldersAPI(self._api)

    @property
    def networks(self):
        '''
        The interface object for the
        :doc:`Networks API <networks>`
        '''
        return NetworksAPI(self._api)

    @property
    def permissions(self):
        '''
        The interface object for the
        :doc:`Permissions API <permissions>`
        '''
        return PermissionsAPI(self._api)

    @property
    def plugins(self):
        '''
        The interface object for the
        :doc:`Plugins API <plugins>`
        '''
        return PluginsAPI(self._api)

    @property
    def scanners(self):
        '''
        The interface object for the
        :doc:`Scanners API <scanners>`
        '''
        return ScannersAPI(self._api)

    @property
    def scanner_groups(self):
        '''
        The interface object for the
        :doc:`Scanner Groups API <scanner_groups>`
        '''
        return ScannerGroupsAPI(self._api)
