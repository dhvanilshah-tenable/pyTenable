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
    plugins
'''
from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.was.folders.api import FoldersAPI
from tenable.io.v3.was.plugins.api import PluginsAPI


class WebApplicationScanning(ExploreBaseEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources under Web Application
    Scanning i.e plugins, scans, folders etc.
    '''

    @property
    def folders(self):
        '''
        The interface object for the
        :doc:`Folders API <folders>`
        '''
        return FoldersAPI(self._api)

    @property
    def plugins(self):
        '''
        The interface object for the
        :doc:`Plugins API <plugins>`
        '''
        return PluginsAPI(self._api)
