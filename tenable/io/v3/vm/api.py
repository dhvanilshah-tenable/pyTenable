from tenable.base.endpoint import APIEndpoint


from tenable.io.cs.images import ImagesAPI
from tenable.io.v3.vm.users import UsersAPI
from tenable.io.cs.reports import ReportsAPI
from tenable.io.cs.repositories import RepositoriesAPI

'''
if we don't inherit the APIEndpoint here then we have to create a constructor 
 -->
'''


class VM_API:

    def __init__(self, api):
        self._api = api

    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vul Mngmnt users APIs <images>`.
        '''
        return UsersAPI(self._api)