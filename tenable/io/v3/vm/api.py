from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.users import UsersAPI


class VulnerabilityManagement(APIEndpoint):

    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vulnerability Management users APIs`.
        '''
        return UsersAPI(self._api)
