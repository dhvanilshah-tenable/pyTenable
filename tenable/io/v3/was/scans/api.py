'''
Scans
=====

The following methods allow for interaction into the Tenable.io
:devportal:`Web Application Scanning v3 scans <was-v2-scans>` API.

Methods available on ``tio.v3.was.scans``:

.. rst-class:: hide-signature
.. autoclass:: ScansAPI
    :members:
'''
from io import BytesIO
from typing import Dict, Optional
from uuid import UUID

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.was.scans.schema import (IteratorSchema, ScanReportSchema,
                                            ScanStatusSchema)
from tenable.utils import dict_clean


class ScansAPI(ExploreBaseEndpoint):
    '''
    This class contains methods related to Networks API
    '''
    _path = 'api/v3/was'
    _conv_json = True

    def delete(self, id: UUID) -> None:
        '''
        Delete a scan.

        :devportal:`was scans: delete scan <was-v2-scans-delete>`

        Args:
            id (UUID): The UUID of the scan for which you want to delete.

        Returns:
            :obj:`None`

        Examples:
            >>> tio.v3.was.scans.delete('91843ecb-ecb8-48a3-b623-d4682c2594')
        '''
        self._delete(f'scans/{id}')

    def details(self, id: UUID) -> Dict:
        '''
        Fetch a scan record.

        :devportal:`was scans: get scan details <was-v2-scans-details>`

        Args:
            id (UUID): The UUID of the scan for which you want to view details.

        Returns:
            obj:`dict`: The record object of the scan.

        Examples:
            >>> tio.v3.was.scans.details('91843ecb-ecb8-48a3-b623-d4682c2594')
        '''
        return super().details(f'scans/{id}')

    def download_report(self, id: UUID,
                        content_type: Optional[str] = 'application/json',
                        fobj: Optional[BytesIO] = None
                        ) -> BytesIO:
        '''
        Download exported scan report.

        :devportal:`was scans: download exported scan
        <was-v2-scans-download-export>`

        Args:
            id (UUID): The UUID of the scan for which you want to view a
                report.
            content_type (str, optional):
                The format you want the report returned in. You can request
                reports in one of the following formats:
                application/json, application/pdf
                text/csv, text/html, text/xml
            fobj (FileObject):
                A file-like object to write the contents of the report to.  If
                none is provided a BytesIO object will be returned with the
                report.

        Returns:
            :obj:`Response`
                The Response object based for the requested attachment.

        Examples:
            >>> with open('report_001.json', 'wb') as report:
            ...     tio.v3.was.scans.download_report(
            ...         '00000000-0000-0000-0000-000000000000',
            ...         'application/json',
            ...         report
            ...     )
        '''
        if not fobj:
            fobj = BytesIO()

        headers = {
            'content_type': content_type
        }
        schema = ScanReportSchema()
        headers = schema.dump(schema.load(headers))
        headers['Content-Type'] = headers.pop('content_type')

        resp = self._get(f'scans/{id}/report', stream=True, headers=headers)

        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:
                fobj.write(chunk)

        fobj.seek(0)
        resp.close()

        return fobj

    def export_report(self, id: UUID, content_type: str = None) -> None:
        '''
        Export scan details.

        :devportal:`was scans: export scan results <was-v2-scans-export>`

        Args:
            id (UUID):
                The UUID of the scan for which you want to generate a report.
            content_type (str, optional):
                The format you want the report returned in.
                Defaults to application/json.
                You can request reports in one of the following formats:
                application/json, application/pdf,
                text/csv, text/html, text/xml

        Returns:
            obj:`None`

        Examples:
            >>> tio.v3.was.scans.export_report(
            ...     '91843ecb-ecb8-48a3-b623-d4682c2594')
        '''
        headers = {
            'content_type': content_type
        }
        schema = ScanReportSchema()
        headers = schema.dump(schema.load(headers))
        headers['Content-Type'] = headers.pop('content_type')
        self._put(f'scans/{id}/report', headers=headers)

    def launch(self, config_id: UUID) -> None:
        '''
        Launch a scan.

        :devportal:`was scans: launch scan <was-v2-scans-launch>`

        Args:
            config_id (UUID):
            The UUID of the scan configuration to use to launch a scan.

        Returns:
            obj:`UUID`: UUID of the scan initiated.

        Examples:
            >>> folder = tio.v3.was.folders.create('New Folder Name')
        '''
        return self._post(f'configs/{config_id}/scans').get('id')

    # TODO: Requires iterator
    def notes(self,
              id: UUID,
              limit: int = 10,
              offset: int = 0,
              sort: str = None
              ) -> None:
        '''
        Get notes of a scan

        :devportal:`was scans: update scan status <was-v2-scans-notes-list>`

        Args:
            id (UUID): The UUID of the scan for which you want to view notes.
            limit (int, optional):
                The number of records to retrieve. If this parameter is
                omitted, Tenable.io uses the default value of 10. The minimum
                value is 0 and the maximum value is 200. If you need to
                retrieve more than 200 records, use the offset value to
                iterate through page responses.
            offset (int, optional):
                The starting record to retrieve. If this parameter is omitted,
                Tenable.io uses the default value of 0.
            sort (str, optional):
                The field you want to use to sort the results by along with the
                sort order. The field is specified first, followed by a colon,
                and the order is specified second (asc or desc).
                For example, name:desc would sort results by the name field in
                descending order.
                If you specify multiple fields, the fields must be separated by
                commas. For example, name:desc,created_at:asc would first sort
                results by the name field in descending order and then by the
                created_at field in ascending order.

        Returns:

        Examples:
            >>> tio.v3.was.scans.notes('91843ecb-ecb8-48a3-b623-d4682c2594',
            ...     20, sort='name:asc')
        '''
        payload = {
            'limit': limit,
            'offset': offset,
            'sort': sort
        }
        schema = IteratorSchema()
        payload = schema.dump(schema.load(payload))
        payload = dict_clean(payload)
        self._get(f'scans/{id}/notes', json=payload)

    # TODO: Requires search iterator
    def search(self, config_id: UUID, **kwargs) -> None:
        '''
        Search for scans.

        :devportal:`was scans: search <was-v2-scans-search>`

        Args:
            config_id (UUID):
                The UUID of the config that was used for the scan.

        Returns:

        Examples:
            >>> tio.v3.was.folders.delete('91843ecb-ecb8-48a3-b623-d4682c28c')
        '''
        raise NotImplementedError(
            'This method will be updated once ExploreSearchIterator is \
                implemented for v3'
        )

    def update_status(self, id: UUID, requested_action: str) -> None:
        '''
        Update the requested_action attribute for a scan. The requested action
        must be valid for the scan's current status. This request creates an
        asynchronous update job.

        :devportal:`was scans: update scan status <was-v2-scans-status-update>`

        Args:
            id (UUID): The UUID of the scan for which you want to update
                status.
            requested_action (str): The action to apply to the scan.
                The only supported action is stop.

        Returns:
            obj:`None`

        Examples:
            >>> tio.v3.was.scans.update_status(
            ...     '91843ecb-ecb8-48a3-b623-d4682c2594'
            ... )
        '''
        schema = ScanStatusSchema()
        payload = {
            'requested_action': requested_action
        }
        payload = schema.dump(schema.load(payload))
        self._patch(f'scans/{id}', json=payload)

    # TODO: Requires search iterator
    def vulnerabilities(self, id: UUID, **kwargs) -> None:
        '''
        Get vulnerabilities for a scan.

        :devportal:`was scans: search vulnerabilities for scan
        <was-v2-scans-details-vulns-search>`

        Args:
            id (UUID): The UUID of the scan for which you want to view notes.

        Returns:

        Examples:
            >>> tio.v3.was.folders.edit(
            ...     '91843ecb-ecb8-48a3-b623-d4682c2594',
            ...     'Updated Folder Name'
            ... )
        '''
        raise NotImplementedError(
            'This method will be updated once ExploreSearchIterator is \
                implemented for v3'
        )
