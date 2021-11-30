'''
Version 3 Base Classes
======================
This class is a iterator for search API call

.. autoclass:: APIResultsIterator
    :members:
'''
from restfly.iterator import APIIterator
from typing import Dict, Tuple, Any


class SearchIterator(APIIterator):
    '''
    The API iterator provides a scalable way to work through result sets of any
    size.  The iterator will walk through each page of data, returning one
    record at a time.  If it reaches the end of a page of records, then it will
    request the next page of information and then continue to return records
    from the next page (and the next, and the next) until the counter reaches
    the total number of records that the API has reported.

    Note that this Iterator is used as a base model for all of the iterators,
    and while the mechanics of each iterator may vary, they should all behave
    to the user in a similar manner.

    Attributes:
        count (int): The current number of records that have been returned
        page (list):
            The current page of data being walked through.  pages will be
            cycled through as the iterator requests more information from the
            API.
        page_count (int): The number of record returned from the current page.
        total (int):
            The total number of records that exist for the current request.
    '''

    total = 1
    _limit = None
    _payload = None
    _path = None
    _resource = None
    _next_token = None

    _pages_total = None
    _pages_requested = 0

    def _get_data(self) -> Tuple[Dict, str]:
        '''
        Request the next page of data
        '''
        path = self._path
        payload = {}
        if not self._next_token:
            payload = self._payload
        else:
            payload["next"] = self._next_token

        resp = self._api._post(path, json=payload)
        return resp, self._resource

    def _get_page(self) -> None:
        '''
        Get the next page of records
        '''

        if self._pages_requested > 0 and not self._next_token:
            self.page = []
        else:
            resp, key = self._get_data()
            self.page_count = 0
            self._pages_requested += 1
            self.page = resp[key]
            pagination = resp.get('pagination')
            self.total = pagination.get('total')
            self._next_token = pagination.get('next')

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self) -> Any:
        '''
        Ask for the next record
        '''
        # If there are no more agent records to return, then we should raise
        # a StopIteration exception.
        if self.count >= self.total:
            raise StopIteration()

        if self.page_count >= len(self.page):
            self._get_page()
            self.page_count = 0
            if len(self.page) == 0:
                raise StopIteration()

        # Get the relevant record, increment the counters, and return the
        # record.
        item = self.page[self.page_count]
        self.count += 1
        self.page_count += 1

        return item
