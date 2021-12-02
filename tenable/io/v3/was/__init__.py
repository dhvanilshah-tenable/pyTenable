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

    attachments
'''
from tenable.io.v3.base.endpoints.explore import APIEndpoint
from tenable.io.v3.was.attachments.api import AttachmentsAPI


class WebApplicationScanning(APIEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources under Web Application
    Scanning i.e plugins, scans, folders etc.
    '''

    @property
    def attachments(self):
        '''
        The interface object for the
        :doc:`Attachments API <attachments>`
        '''
        return AttachmentsAPI(self._api)
