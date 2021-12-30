'''
Scan Bridge
===========

The following class allows to send TenableIO scans to a TenableSC.

Methods available on ``tio.utilities.scan_bridge``:

.. rst-class:: hide-signature
.. autoclass:: ScanBridge
    :members:
'''
import os

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class ScanBridge(ExploreBaseEndpoint):
    '''
    This will contain all methods related to Users
    '''
    def __init__(self, tsc, tio):
        self.tio = tio
        self.tsc = tsc

    def move(self, scan_id: int, repo_id: int):
        '''
        This methods sends the TenableIO scan details to a TenableSC repo ID

        Args:
            scan_id (int):
                The TenableIO scan_id whose details is to be migrated.
            repo_id (int):
                The repo_id of Tenable SC instance where scan details
                will be imported.
        Example:
            Move Scan IDs 13, 5091 and 5057 from T.io to T.sc at 192.168.1.200
            and use repo ID 54.
        '''
        with open(f'{scan_id}.nessus', 'wb') as nessus:
            self.tio.scans.export(scan_id, fobj=nessus)
        with open(f'{scan_id}.nessus') as file:
            self.tsc.scan_instances.import_scan(file, repo_id)

        os.remove(f'{scan_id}.nessus')
