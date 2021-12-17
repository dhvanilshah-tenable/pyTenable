'''
Filters
=======

The following methods allow for interaction into the Tenable.io
:devportal:`filters <filters-1>` API endpoints.

Methods available on ``tio.v3.vm.filters``:

.. rst-class:: hide-signature
.. autoclass:: FiltersAPI
    :members:
'''
from typing import Dict

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class FiltersAPI(ExploreBaseEndpoint):
    '''
    This will contain all methods related to filters
    '''
    _cache: dict = dict()
    _path: str = 'filters'
    _conv_json: bool = True

    @staticmethod
    def _normalize(filterset):
        '''
        Converts the filters into an easily pars-able dictionary
        '''
        filters = dict()
        for item in filterset:
            datablock = {
                'operators': item['operators'],
                'choices': None,
                'pattern': None,
            }

            # If there is a list of choices available, then we need to parse
            # them out and only pull back the usable values as a list
            if 'list' in item['control']:
                # There is a lack of consistency here.
                # In some cases the 'list' is a list of dictionary items,
                # and in other cases the 'list' is a list of string values.
                if isinstance(item['control']['list'][0], dict):
                    if 'value' in item['control']['list'][0]:
                        key = 'value'
                    else:
                        key = 'id'
                    datablock['choices'] = [
                        str(i[key]) for i in item['control']['list']
                    ]
                elif isinstance(item['control']['list'], list):
                    datablock['choices'] = [
                        str(i) for i in item['control']['list']
                    ]
            if 'regex' in item['control']:
                datablock['pattern'] = item['control']['regex']
            filters[item['name']] = datablock
        return filters

    def _use_cache(self, name, path, field_name='filters', normalize=True):
        '''
        Leverages the filter cache and will return the results as expected.
        '''
        if name not in self._cache:
            self._cache[name] = self._get(path)[field_name]
        if normalize:
            return self._normalize(self._cache[name])
        return self._cache[name]

    def agents_filters(self, normalize=True) -> Dict:
        '''
        Returns agent filters.

        :devportal:`filters: agents-filters <io-filters-agents-list>`

        Returns:
            :obj:`dict`:
                Filter resource dictionary

        Examples:
            >>> filters = tio.v3.vm.filters.agents_filters()
        '''
        return self._use_cache('agents', 'scans/agents', normalize=normalize)

    def credentials_filters(self, normalize=True) -> Dict:
        '''
        Returns the individual scan filters.

        :devportal:`filters: credentials <io-filters-credentials-list>`

        Returns:
            :obj:`dict`:
                Filter resource dictionary

        Examples:
            >>> filters = tio.v3.vm.filters.credentials_filters()
        '''
        return self._use_cache('scan', 'credentials', normalize=normalize)

    def scan_filters(self, normalize=True) -> Dict:
        '''
        Returns the individual scan filters.

        :devportal:`filters: scan <io-filters-scan-list>`

        Returns:
            :obj:`dict`:
                Filter resource dictionary

        Examples:
            >>> filters = tio.v3.vm.filters.scan_filters()
        '''
        return self._use_cache('scan', 'scans/reports', normalize=normalize)

    def scan_history_filters(self, normalize=True) -> Dict:
        '''
        Returns the individual scan history filters.

        :devportal:`filters: scan-history <io-filters-scan-history-list>`

        Returns:
            :obj:`dict`:
                Filter resource dictionary

        Examples:
            >>> filters = tio.v3.vm.filters.scan_history_filter()
        '''
        return self._use_cache(
            'scan',
            'scans/reports/history',
            normalize=normalize
        )

    def workbench_asset_filters(self, normalize=True):
        '''
        Returns the asset workbench filters.

        :devportal:`workbenches: assets-filters <filters-assets-filter>`

        Returns:
            :obj:`dict`:
                Filter resource dictionary

        Examples:
            >>> filters = tio.v3.vm.filters.workbench_asset_filters()
        '''
        return self._use_cache(
            'asset',
            'workbenches/assets',
            normalize=normalize
        )

    def workbench_vuln_filters(self, normalize=True):
        '''
        Returns the vulnerability workbench filters

        :devportal:`workbenches: vulnerabilities-filters
        <workbenches-vulnerabilities-filters>`

        Returns:
            :obj:`dict`:
                Filter resource dictionary

        Examples:
            >>> filters = tio.v3.vm.filters.workbench_vuln_filters()
        '''
        return self._use_cache(
            'vulns',
            'workbenches/vulnerabilities',
            normalize=normalize
        )
