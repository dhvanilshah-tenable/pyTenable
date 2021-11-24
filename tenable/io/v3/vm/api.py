from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.plugins import PluginsAPI

'''
VulnerabilityManagement
==================

The following sub-package allows for interaction with the Tenable.io
Vulnerability Management APIs.

.. rst-class:: hide-signature
.. autoclass:: VulnerabilityManagement
    :members:

.. toctree::
    :hidden:
    :glob:
    
    plugins
'''


class VulnerabilityManagement(APIEndpoint):

    @property
    def plugins(self):
        """
        The interface object for plugin API
        Returns:
        """
        return PluginsAPI(self._api)
