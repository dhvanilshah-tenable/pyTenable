from tenable.base.endpoint import APIEndpoint
from .vm import VulnerabilityManagement

class V3class(APIEndpoint):  # noqa: PLR0904
    
    @property
    def vm(self):
        return VulnerabilityManagement(self._api)

