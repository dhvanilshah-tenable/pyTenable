'''
Filters
=======

The following methods allow for interaction into the Tenable.io
:devportal:`Web Application Scanning v3 filters <filters-2>` API.

Methods available on ``tio.v3.was.filters``:

.. rst-class:: hide-signature
.. autoclass:: FiltersAPI
    :members:
'''
from typing import List
from uuid import UUID

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class FiltersAPI(ExploreBaseEndpoint):
    _path = 'api/v3/was'
    _conv_json = True

    def scans_filters(self, config_id: UUID) -> List:
        '''
        Lists the filtering capabilities available for scans for endpoints
        that support scan filtering.

        :devportal:`was filters: List scan filters
        <was-v2-filters-scans-list>`

        Args:
            config_id (UUID):
                The UUID of the scan configuration that was used for the scan.

        Returns:
            :obj:`list`: List of filters available for scans.

        Examples:
            >>> for filter in tio.v3.was.filters.scans_filters():
            ...     pprint(filter)
        '''
        return self._get(f'configs/{config_id}/scans/filters')['filters']

    def scan_configurations_filters(self) -> List:
        '''
        Lists the filtering capabilities available for scan configurations for
        endpoints that support scan configuration filtering.

        :devportal:`was filters: List scan configuration filters
        <was-v2-filters-scan-configs-list>`

        Returns:
            :obj:`list`: List of filters available for scan configurations.

        Examples:
            >>> for filter in tio.v3.was.filters.scan_configurations_filters():
            ...     pprint(filter)
        '''
        return self._get('configs/filters')['filters']

    def scan_vulnerabilities_filters(self, scan_id: UUID) -> List:
        '''
        Lists the filtering capabilities available for vulnerability findings
        on a given scan for endpoints that support vulnerability filtering.

        :devportal:`was filters: List vulnerability filters for scan
        <was-v2-filters-vulns-scan-list>`

        Args:
            scan_id (UUID):
                The UUID of the scan configuration that was used for the scan.

        Returns:
            :obj:`list`:
                List of filters available for vulnerability findings on a given
                scan.

        Examples:
            >>> for filter in (tio.v3.was.filters.
            ...     scan_vulnerabilities_filters()):
            ...     pprint(filter)
        '''
        return self._get(f'scans/{scan_id}/vulnerabilities/filters')['filters']

    def user_templates_filters(self) -> List:
        '''
        Lists the filtering capabilities available for user-defined templates
        for endpoints that support user-defined template filtering.

        :devportal:`was filters: List user-defined template filters
        <was-v2-filters-user-templates-list>`

        Returns:
            :obj:`list`: List of filters available for user-defined templates.

        Examples:
            >>> for filter in tio.v3.was.filters.user_templates_filters():
            ...     pprint(filter)
        '''
        return self._get(f'user-templates/filters')['filters']

    def vulnerabilities_filters(self) -> List:
        '''
        Lists the filtering capabilities available for vulnerability findings
        for endpoints that support vulnerability filtering.

        :devportal:`was filters: List vulnerability filters
        <was-v2-filters-vulns-list>`

        Returns:
            :obj:`list`: List of filters available for vulnerability findings.

        Examples:
            >>> for filter in tio.v3.was.filters.vulnerabilities_filters():
            ...     pprint(filter)
        '''
        return self._get(f'vulnerabilities/filters')['filters']
