from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.users import UsersAPI

'''
VulnerabilityManagement
==================

The following sub-package allows for interaction with the Tenable.io
Vulnerability Management APIs.

.. rst-class:: hide-signature
.. autoclass:: VulnerabilityManagement
    :members:

.. toctree::
    :hidden:
    :glob:

    users
'''


class VulnerabilityManagement(APIEndpoint):

    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vulnerability Management users APIs`.
        '''
        return UsersAPI(self._api)
