"""
Version3API
===========
The following sub-package allows for interaction with the Tenable.io
Version3API APIs.
.. rst-class:: hide-signature
.. autoclass:: Version3API
    :members:
.. toctree::
    :hidden:
    :glob:
    groups
"""
from tenable.base.endpoint import APIEndpoint

from .groups import GroupsAPI


class Version3API(APIEndpoint):
    """
    This will contain property for all resources/app under io
    i.e Container Security, Web Application Security.
    """

    # pylint: disable=too-few-public-methods
    @property
    def groups(self):
        """
        The interface object for the Groups APIs
        :doc:`Tenable.io.v3.groups Groups APIs <groups>`.
        """
        return GroupsAPI(self._api)
