
from typing import Dict, List, Optional
from requests import Response

# from tenable.io.v3.vm.scanners import ScannersAPI
from .scanners import ScannersAPI
from tenable.io.v3.base_pkg.endpoints.uw import UWBaseEndpoint
from tenable.base.platform import APIPlatform
from tenable.io.base import TIOEndpoint


class VulnerabilityManagement(TIOEndpoint):  # noqa: PLR0904
    
    @property
    def scanners(self):
        return ScannersAPI(self._api)

