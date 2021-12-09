'''
Vulnerability Management
========================

The following API's are available for interaction
under Vulnerability Management platform.

Methods available on ``tio.v3.vm``:


.. rst-class:: hide-signature
.. autoclass:: VulnerabilityManagement
    :members:

.. toctree::
    :hidden:
    :glob:

    credentials
    scanners
'''
from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.credentials import CredentialsAPI

from .scanners import ScannersAPI


class VulnerabilityManagement(APIEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources
    under Vulnerability Management
    i.e assets, agents, scanners etc.
    '''

    @property
    def credentials(self):
        '''
        The interface object for the
        :doc:`Credentials API <credentials>`
        '''
        return CredentialsAPI(self._api)

    @property
    def scanners(self):
        '''
        The interface object for the
        :doc:`Scanners API <scanners>`
        '''
        return ScannersAPI(self._api)
