'''
.. autoclass:: TenableIO

.. automodule:: tenable.io.access_groups
.. automodule:: tenable.io.access_groups_v2
.. automodule:: tenable.io.agent_config
.. automodule:: tenable.io.agent_exclusions
.. automodule:: tenable.io.agent_groups
.. automodule:: tenable.io.agents
.. automodule:: tenable.io.assets
.. automodule:: tenable.io.audit_log
.. automodule:: tenable.io.credentials
.. automodule:: tenable.io.editor
.. automodule:: tenable.io.exclusions
.. automodule:: tenable.io.exports
.. automodule:: tenable.io.files
.. automodule:: tenable.io.filters
.. automodule:: tenable.io.folders
.. automodule:: tenable.io.groups
.. automodule:: tenable.io.networks
.. automodule:: tenable.io.permissions
.. automodule:: tenable.io.plugins
.. automodule:: tenable.io.policies
.. automodule:: tenable.io.scanner_groups
.. automodule:: tenable.io.scanners
.. automodule:: tenable.io.scans
.. automodule:: tenable.io.remediation_scans
.. automodule:: tenable.io.server
.. automodule:: tenable.io.session
.. automodule:: tenable.io.tags
.. automodule:: tenable.io.target_groups
.. automodule:: tenable.io.users
.. automodule:: tenable.io.workbenches

Raw HTTP Calls
==============

Even though the ``TenableIO`` object pythonizes the Tenable.io API for you,
there may still bee the occasional need to make raw HTTP calls to the IO API.
The methods listed below aren't run through any naturalization by the library
aside from the response code checking.  These methods effectively route
directly into the requests session.  The responses will be Response objects
from the ``requests`` library.  In all cases, the path is appended to the base_pkg
``url`` parameter that the ``TenableIO`` object was instantiated with.

Example:

.. code-block:: python

   resp = tio.get('scans')

.. py:module:: tenable.io
.. rst-class:: hide-signature
.. py:class:: TenableIO

    .. automethod:: get
    .. automethod:: post
    .. automethod:: put
    .. automethod:: delete
'''
from typing import Dict, List, Optional
from requests import Response
from tenable.base.platform import APIPlatform
from .scanners import ScannersAPI


class TenableIO(APIPlatform):  # noqa: PLR0904
    '''
    The Tenable.io object is the primary interaction point for users to
    interface with Tenable.io via the pyTenable library.  All of the API
    endpoint classes that have been written will be grafted onto this class.

    Args:
        access_key (str, optional):
            The user's API access key for Tenable.io  If an access key isn't
            specified, then the library will attempt to read the environment
            variable ``TIO_ACCESS_KEY`` to acquire the key.
        secret_key (str, optional):
            The user's API secret key for Tenable.io  If a secret key isn't
            specified, then the library will attempt to read the environment
            variable ``TIO_SECRET_KEY`` to acquire the key.
        url (str, optional):
            The base_pkg URL that the paths will be appended onto.  The default
            is ``https://cloud.tenable.com``
        retries (int, optional):
            The number of retries to make before failing a request.  The
            default is ``5``.
        backoff (float, optional):
            If a 429 response is returned, how much do we want to backoff
            if the response didn't send a Retry-After header.  The default
            backoff is ``1`` second.
        vendor (str, optional):
            The vendor name for the User-Agent string.
        product (str, optional):
            The product name for the User-Agent string.
        build (str, optional):
            The version or build identifier for the User-Agent string.
        timeout (int, optional):
            The connection timeout parameter informing the library how long to
            wait in seconds for a stalled response before terminating the
            connection.  If unspecified, the default is 120 seconds.

    Examples:
        Basic Example:

        >>> from tenable.io import TenableIO
        >>> tio = TenableIO('ACCESS_KEY', 'SECRET_KEY')

        Example with proper identification:

        >>> tio = TenableIO('ACCESS_KEY', 'SECRET_KEY',
        >>>     vendor='Company Name',
        >>>     product='My Awesome Widget',
        >>>     build='1.0.0')

        Example with proper identification leveraging environment variables for
        access and secret keys:

        >>> tio = TenableIO(
        >>>     vendor='Company Name', product='Widget', build='1.0.0')
    '''
    _env_base = 'TIO'
    _tzcache = None
    _url = 'https://cloud.tenable.com'
    _timeout = 120

    def __init__(self,
                 access_key: Optional[str] = None,
                 secret_key: Optional[str] = None,
                 **kwargs
                 ):
        if access_key:
            kwargs['access_key'] = access_key
        if secret_key:
            kwargs['secret_key'] = secret_key
        super().__init__(**kwargs)

    def _retry_request(self,
                       response: Response,
                       retries: int,
                       **kwargs) -> Dict:
        '''
        If the call is retried, we will need to set some additional headers
        '''
        kwargs['headers'] = kwargs.get('headers', {})
        # if the request uuid exists in the response, then we will send the
        # uuid back so that there is solid request chain in the Tenable.io
        # platform logs.
        request_uuid = response.headers.get('X-Tio-Last-Request-Uuid')
        if request_uuid:
            kwargs['headers']['X-Tio-Last-Request-Uuid'] = request_uuid

        # We also need to return the number of times that we have attempted to
        # retry this call.
        kwargs['headers']['X-Tio-Retry-Count'] = str(retries)

        # Return the keyword arguments back to the caller.
        return kwargs

    @property
    def _tz(self):
        '''
        As we will be using the timezone listing in a lot of parameter
        checking, we should probably cache the response as a private attribute
        to speed up checking times.
        '''
        if not self._tzcache:
            self._tzcache = self.scans.timezones()
        return self._tzcache

    @property
    def scanners(self):
        return ScannersAPI(self)

