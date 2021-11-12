
from restfly.endpoint import APIEndpoint
from .scanners import ScannersAPI


class VulnerabilityManagement(APIEndpoint):  # noqa: PLR0904
    
    @property
    def scanners(self):
        return ScannersAPI(self._api)

