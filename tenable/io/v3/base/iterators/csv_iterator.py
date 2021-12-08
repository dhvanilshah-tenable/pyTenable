'''
Version 3 Classes
======================
This class is a iterator for search API call

.. autoclass:: CSVIterator
    :members:
'''
from typing import Any

from tenable.io.v3.base.iterators.iterator import APIResultIterator


class CSVIterator(APIResultIterator):
    '''
    The CSV iterator provides a scalable way to work through result sets
    of any
    size.  The iterator will walk through each page of data, returning one
    page at a time. On each next call it will fetch the page from the server
    and return it to the user with the row headers of csv data. It will
    keep on fetching the records from the server until we keep getting next
    token.

    Note that this Iterator is used as a base model for all of the csv
    iterators, and while the mechanics of each iterator may vary,
    they should all behave to the user in a similar manner.

    Attributes:
        page (str):
            The current page of data being walked through. pages will be
            cycled through as the iterator requests more information from the
            API.
        _next_token (str):
            Token for next records to fetch from the server
    '''

    _limit = None
    _payload = None
    _path = None
    _next_token = None
    _resource = None

    _pages_requested = 0

    def _get_data(self):
        '''
        Request the next page of data
        '''
        path = self._path
        payload = {}
        if not self._next_token:
            payload = self._payload
        else:
            payload["next"] = self._next_token

        resp = self._api.post(path, json=payload, headers={
            'Accept': 'text/csv'})
        return resp

    def _get_page(self) -> None:
        '''
        Get the next page of records
        '''

        if self._pages_requested > 0 and not self._next_token:
            self.page = []
        else:
            resp = self._get_data()
            self.page_count = 0
            self._pages_requested += 1
            self.page = resp.text
            self._next_token = resp.headers.get('X-Continuation-Token')
            # this below should be executed for first response only
            if self._pages_requested == 1 and self._next_token:
                self.row_headers = self.page.partition('\n')[0]

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self) -> Any:
        '''
        Ask for the next record
        '''

        # new server request will be initiated on every next call.
        # when size of text data will be zero then execution will be stopped.
        # row headers will be appended to each page received after first
        # pagination.
        self._get_page()
        if len(self.page) == 0:
            raise StopIteration()

        return self._add_headers()

    def _add_headers(self):
        if self._pages_requested > 1 and isinstance(self.page, str):
            return self.row_headers + '\n' + self.page
        else:
            return self.page
