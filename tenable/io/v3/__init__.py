from tenable.base.endpoint import APIEndpoint
from .vm import VulnerabilityManagement

class V3class(APIEndpoint):  # noqa: PLR0904
    """
    This will contain property for all resources/app under io i.e Container Security, Web Application Security.
    """
    @property
    def vm(self):
        return VulnerabilityManagement(self._api)

