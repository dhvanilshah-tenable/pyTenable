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

    plugins
    scanners
    vulnerability
'''
from restfly.endpoint import APIEndpoint

from .plugins import PluginsAPI
from .scanners import ScannersAPI
from .vulnerability import VulnerabilityAPI


class VulnerabilityManagement(APIEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources
    under Vulnerability Management
    i.e assets, agents, scanners etc.
    '''

    @property
    def plugins(self):
        '''
        The interface object for the
        :ref:`Plugins API <plugins>`
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
    def vulnerability(self):
        '''
        The interface object for the
        :doc:`Vulnerability API <vulnerability>`
        '''
        pass
        return VulnerabilityAPI(self._api)
