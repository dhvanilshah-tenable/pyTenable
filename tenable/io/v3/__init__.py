'''
Version3 API
============

The following sub-package allows for interaction with the Tenable.io
Version3API APIs.

.. rst-class:: hide-signature
.. autoclass:: Version3API
    :members:

.. toctree::
    :hidden:
    :glob:

    users
    vm/index
    was/index
'''
from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.users import UsersAPI
from tenable.io.v3.vm.api import VulnerabilityManagement
from tenable.io.v3.was import WebApplicationScanning


class Version3API(APIEndpoint):  # noqa: PLR0904
    '''
    This will contain property for all resources/app under io
    i.e Container Security, Web Application Security.
    '''
    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io users APIs`.
        '''
        return UsersAPI(self._api)

    @property
    def vm(self):
        '''
        The interface object for the Vulnerability Management API's
        '''
        return VulnerabilityManagement(self._api)

    @property
    def was(self):
        '''
        The interface object for the Web Application API's
        '''
        return WebApplicationScanning(self._api)
