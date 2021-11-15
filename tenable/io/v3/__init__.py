"""
Version3API
===========
"""
from tenable.base.endpoint import APIEndpoint

from .assets import AssetsAPI


class Version3API(APIEndpoint):  # noqa: PLR0904
    """
    This will contain property for all resources/app under io
    i.e Container Security, Web Application Security.
    """

    # pylint: disable=too-few-public-methods
    @property
    def assets(self):
        """
        The interface object for the Assets API's
        """
        return AssetsAPI(self._api)
