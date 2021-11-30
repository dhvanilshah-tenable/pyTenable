'''
API's under Web Application Scanning
'''
from restfly.endpoint import APIEndpoint

from tenable.io.v3.was.folders import FoldersAPI


class WebApplicationScanning(APIEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources under Web Application
    Scanning i.e plugins, scans, folders etc.
    '''

    @property
    def folders(self):
        return FoldersAPI(self._api)
