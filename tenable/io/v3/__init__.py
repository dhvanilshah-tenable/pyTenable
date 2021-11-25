'''
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

    assets
    users


'''
from tenable.base.endpoint import APIEndpoint
from .assets import AssetsAPI
from .users import UsersAPI


class Version3API(APIEndpoint):
    '''
    This will contain property for all resources/app under io
    i.e Container Security, Web Application Security.
    '''

    @property
    def assets(self):
        """
        The interface object for the Assets APIs
        :doc:`Tenable.io.v3.assets Assets APIs <assets>`.
        """
        return AssetsAPI(self._api)

    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io users APIs`.
        '''
        return UsersAPI(self._api)
