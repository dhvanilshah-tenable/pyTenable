
from restfly.endpoint import APIEndpoint
from .assets import AssetsAPI


class VulnerabilityManagement(APIEndpoint):  # noqa: PLR0904
    """
    This class will contain property for all resources under Vulnerability Management i.e assets, agents, scanners etc.
    """
    @property
    def assets(self):
        return AssetsAPI(self._api)
