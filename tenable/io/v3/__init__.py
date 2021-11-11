
from typing import Dict, List, Optional
from requests import Response

from .vm import VulnerabilityManagement


class V3class():  # noqa: PLR0904
    
    @property
    def vm(self):
        return VulnerabilityManagement(self)

# 3 import options for child class
# APIPlatform
# APIEndpoint
# UWBaseEndpoint
