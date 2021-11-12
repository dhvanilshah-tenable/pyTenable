from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.api import VulnerabilityManagement


class Version3API(APIEndpoint):

    @property
    def vm(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vul Management APIs`.
        '''
        return VulnerabilityManagement(self._api)
