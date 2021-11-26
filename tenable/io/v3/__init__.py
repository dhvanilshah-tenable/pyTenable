from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.api import VulnerabilityManagement
from tenable.io.v3.users import UsersAPI

'''
Version3API
==================

The following sub-package allows for interaction with the Tenable.io
Version3API APIs.

.. rst-class:: hide-signature
.. autoclass:: Version3API
    :members:

.. toctree::
    :hidden:
    :glob:

    vm
    users
'''


class Version3API(APIEndpoint):
    '''
    Version 3 API base class
    '''

    @property
    def vm(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vul Management APIs`.
        '''
        return VulnerabilityManagement(self._api)

    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io users APIs`.
        '''
        return UsersAPI(self._api)
