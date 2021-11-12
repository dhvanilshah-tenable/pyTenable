"""
Version3API
===========
"""
from tenable.base.endpoint import APIEndpoint

from .vm.api import VulnerabilityManagement


class Version3API(APIEndpoint):  # noqa: PLR0904
    """
    This will contain property for all resources/app under io
    i.e Container Security, Web Application Security.
    """
    # pylint: disable=invalid-name, too-few-public-methods
    @property
    def vm(self):
        """
        The interface object for the Vulnerability Management API's
        """
        return VulnerabilityManagement(self._api)
