from tenable.base.endpoint import APIEndpoint
from .vm.api import VulnerabilityManagement

class Version3API(APIEndpoint):  # noqa: PLR0904
    """
    This will contain property for all resources/app under io i.e Container Security, Web Application Security.
    """
    @property
    def vm(self):
        return VulnerabilityManagement(self._api)

