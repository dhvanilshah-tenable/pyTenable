'''
.. _vm-reference-label:

Vulnerability Management
========================

The following API's are available for interaction under Vulnerability Management platform.

Methods available on ``tio.v3.vm``:


.. rst-class:: hide-signature
.. autoclass:: VulnerabilityManagement
    :members:
.. toctree::

    :hidden:
    :glob:

    plugins
    scanners
'''
from restfly.endpoint import APIEndpoint
from .scanners import ScannersAPI
from .plugins import PluginsAPI


class VulnerabilityManagement(APIEndpoint):  # noqa: PLR0904
    """
    This class will contain property for all resources
    under Vulnerability Management
    i.e assets, agents, scanners etc.
    """

    @property
    def scanners(self):
        '''
        The interface object for the
        :ref:`scanners-reference-label`
        '''
        return ScannersAPI(self._api)

    @property
    def plugins(self):
        '''
        The interface object for the
        :ref:`Plugins API <plugins>`
        '''
        return PluginsAPI(self._api)