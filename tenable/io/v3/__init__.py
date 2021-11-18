from tenable.base.endpoint import APIEndpoint
from tenable.io.v3.vm.api import VulnerabilityManagement

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
