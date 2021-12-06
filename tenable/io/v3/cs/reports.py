'''
Reports
=======

The following methods allow for interaction into the Tenable.io
Container Security :devportal:`report <cs-v2-reports>` API endpoints.

Methods available on ``tio.cs.reports``:

.. rst-class:: hide-signature
.. autoclass:: ReportsAPI
    :members:
'''
from typing import Dict

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint


class ReportsAPI(ExploreBaseEndpoint):  # noqa: PLR0903
    _path = 'container-security/api/v2/reports'
    _box = True
    _box_attrs = {'camel_killer_box': True}
    _conv_json = True

    def report(self, repository: str, image: str, tag: str) -> Dict:
        '''
        Returns the report for the specified image.

        :devportal:`API Documentation <container-security-v3-get-image-report>`

        Args:
            repository:
                The repository name.
            image:
                The image name.
            tag:
                The tag name.

        Returns:
            :obj:`dict`:
                Vulnerability report for the specified image.
        Examples:

            >>> tio.v3.cs.reports.report('centos', '7', 'latest')
        '''
        return self._get(f'{repository}/{image}/{tag}')
