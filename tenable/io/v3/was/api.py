'''
Web Application Scanning
========================

The following API's are available for interaction under Web Application
Scanning

Methods available on ``tio.v3.was``:


.. rst-class:: hide-signature
.. autoclass:: WebApplicationScanning
    :members:

.. toctree::
    :hidden:
    :glob:

    folders
    vulnerability
'''
from restfly.endpoint import APIEndpoint

from tenable.io.v3.was.folders import FoldersAPI

from .vulnerability import VulnerabilityAPI


class WebAppScanning(APIEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources
    under Web Application Scanning
    i.e attachments, configurations, folders etc.
    '''

    @property
    def folders(self):
        '''
        The interface object for the
        :doc:`Folders API <folders>`
        '''
        return FoldersAPI(self._api)

    @property
    def vulnerability(self):
        '''
        The interface object for the
        :doc:`Vulnerability API <vulnerability>`
        '''
        pass
        return VulnerabilityAPI(self._api)
