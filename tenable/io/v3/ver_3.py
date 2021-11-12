
from tenable.io.v3.vm.api import VM_API


class Version3_API:

    def __init__(self, api):
        self._api = api

    @property
    def vm(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vul Mngmnt APIs <images>`.
        '''
        return VM_API(self._api)