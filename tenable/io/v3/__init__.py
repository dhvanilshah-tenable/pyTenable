
from typing import Dict, List, Optional
from requests import Response

from .vm import VulnerabilityManagement
from tenable.base.platform import APIPlatform
from tenable.io.base import TIOEndpoint

class V3class(TIOEndpoint):  # noqa: PLR0904
    
    @property
    def vm(self):
        return VulnerabilityManagement(self._api)

