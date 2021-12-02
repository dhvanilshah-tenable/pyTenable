'''
Web Application Scanning
========================

The following API's are available for interaction under Web Application Scanning platform.

Methods available on ``tio.v3.vm``:


.. rst-class:: hide-signature
.. autoclass:: WebAppScanning
    :members:

.. toctree::
    :hidden:
    :glob:

    vulnerability
'''
from restfly.endpoint import APIEndpoint
from .vulnerability import VulnerabilityAPI


class WebAppScanning(APIEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources
    under Web Application Scanning
    i.e attachments, configurations, folders etc.
    '''

    @property
    def vulnerability(self):
        '''
        The interface object for the
        :doc:`Vulenrability API <vulnerability>`
        '''
        pass
        return VulnerabilityAPI(self._api)
