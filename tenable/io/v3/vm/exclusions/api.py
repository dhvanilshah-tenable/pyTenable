'''
Exclusions
==========

The following methods allow for interaction into the Tenable.io
:devportal:`exclusions <exclusions>`
API endpoints.

Methods available on ``tio.v3.vm.exclusions``:

.. rst-class:: hide-signature
.. autoclass:: ExclusionsAPI
    :members:
'''

from datetime import datetime
from typing import BinaryIO, Dict, List, Optional
from uuid import UUID

from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.vm.exclusions.schema import ExclusionSchema


class ExclusionsAPI(ExploreBaseEndpoint):
    '''
    This will contain all methods related to exclusions
    '''
    _path: str = 'api/v3/exclusions'
    _conv_json: bool = True
    _schema = ExclusionSchema()

    def create(self,
               name: str,
               members: List,
               start_time: Optional[str] = None,
               end_time: Optional[str] = None,
               description: Optional[str] = None,
               frequency: Optional[str] = None,
               interval: Optional[int] = None,
               weekdays: Optional[List] = None,
               day_of_month: Optional[int] = None,
               enabled: Optional[bool] = True,
               network_id: Optional[UUID] = None
               ) -> Dict:
        '''
        Create a scan target exclusion.

        :devportal:`exclusions: create <exclusions-create>`

        Args:
            name (str): The name of the exclusion to create.
            members (list):
                The exclusions members.  Each member should be a string with
                either a FQDN, IP Address, IP Range, or CIDR.
            start_time (datetime): When the exclusion should start.
            end_time (datetime): When the exclusion should end.
            description (str, optional):
                Some further detail about the exclusion.
            frequency (str, optional):
                The frequency of the rule.The string inputted will be up-cased
                Valid values are: ``ONETIME``, ``DAILY``, ``WEEKLY``,
                ``MONTHLY``, ``YEARLY``.
                Default value is ``ONETIME``.
            interval (int, optional):
                The interval of the rule.  The default interval is 1
            weekdays (list, optional):
                List of 2-character representations of the days of the week to
                repeat the frequency rule on.  Valid values are:
                *SU, MO, TU, WE, TH, FR, SA*
                Default values: ``['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']``
            day_of_month (int, optional):
                The day of the month to repeat a **MONTHLY** frequency rule on.
                The default is today.
            enabled (bool, optional):
                If enabled is true, the exclusion schedule is active.
                If enabled is false, the exclusion is "Always Active"
                    The default value is ``True``
            network_id (uuid, optional):
                The ID of the network object associated with scanners
                where Tenable.io applies the exclusion.

        Returns:
            :obj:`dict`:
                Dictionary of the newly minted exclusion.

        Examples:
            Creating a one-time exclusion:

            >>> from datetime import datetime, timedelta
            >>> exclusion = tio.v3.vm.exclusions.create(
            ...     'Example One-Time Exclusion',
            ...     ['127.0.0.1'],
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a daily exclusion:

            >>> exclusion = tio.v3.vm.exclusions.create(
            ...     'Example Daily Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='daily',
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a weekly exclusion:

            >>> exclusion = tio.v3.vm.exclusions.create(
            ...     'Example Weekly Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='weekly',
            ...     weekdays=['mo', 'we', 'fr'],
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a monthly esxclusion:

            >>> exclusion = tio.v3.vm.exclusions.create(
            ...     'Example Monthly Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='monthly',
            ...     day_of_month=1,
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))

            Creating a yearly exclusion:

            >>> exclusion = tio.v3.vm.exclusions.create(
            ...     'Example Yearly Exclusion',
            ...     ['127.0.0.1'],
            ...     frequency='yearly',
            ...     start_time=datetime.utcnow(),
            ...     end_time=datetime.utcnow() + timedelta(hours=1))
        '''

        # construct payload schedule based on enable
        if enabled is True:
            if isinstance(frequency, str):
                frequency = frequency.upper()

            rrules = {
                'freq': frequency or 'ONETIME',
                'interval': interval or 1
            }

            if rrules['freq'] == 'WEEKLY':
                rrules['byweekday'] = weekdays or [
                    'SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'
                ]

            if rrules['freq'] == 'MONTHLY':
                rrules['bymonthday'] = day_of_month or datetime.today().day

            schedule: dict = {
                'enabled': True,
                'starttime': start_time,
                'endtime': end_time,
                'rrules': rrules
            }
        elif enabled is False:
            schedule = {'enabled': False}
        else:
            raise TypeError('enabled must be a boolean value.')

        # Next we need to construct the rest of the payload
        payload = {
            'name': name,
            'members': members,
            'description': description or '',
            'network_id': network_id or '00000000-0000-0000-0000-000000000000',
            'schedule': schedule
        }

        # Let's validate the payload using Mershmallow schema
        payload = self._schema.dump(self._schema.load(payload))

        # And now to make the call and return the data.
        return self._post(json=payload)

    def delete(self, exclusion_id: int) -> None:
        '''
        Delete a scan target exclusion.

        :devportal:`exclusions: delete <exclusions-delete>`

        Args:
            exclusion_id (int): The exclusion identifier to delete

        Returns:
            :obj:`None`:
                The exclusion was successfully deleted.

        Examples:
            >>> tio.v3.vm.exclusions.delete(1)
        '''
        self._delete(f'{exclusion_id}')

    def details(self, exclusion_id: int) -> Dict:
        '''
        Retrieve the details for a specific scan target exclusion.

        :devportal:`exclusions: details <exclusions-details>`

        Args:
            exclusion_id (int): The exclusion identifier.

        Returns:
            :obj:`dict`:
                The exclusion record requested.

        Examples:
            >>> exclusion = tio.v3.vm.exclusions.details(1)
            >>> pprint(exclusion)
        '''
        return self._get(f'{exclusion_id}')

    def edit(self,
             exclusion_id: int,
             name: Optional[str] = None,
             members: Optional[List] = None,
             start_time: Optional[str] = None,
             end_time: Optional[str] = None,
             description: Optional[str] = None,
             frequency: Optional[str] = None,
             interval: Optional[int] = None,
             weekdays: Optional[List] = None,
             day_of_month: Optional[int] = None,
             enabled: Optional[bool] = None,
             network_id: Optional[UUID] = None
             ) -> Dict:
        '''
        Edit an existing scan target exclusion.

        :devportal:`exclusions: edit <exclusions-edit>`

        The edit function will first gather the details of the exclusion that
        will be edited and will overlay the changes on top.  The result will
        then be pushed back to the API to modify the exclusion.

        Args:
            exclusion_id (int): The id of the exclusion object in Tenable.io
            name (str, optional): The name of the exclusion to create.
            members (list, optional):
                The exclusions members.  Each member should be a string with
                either a FQDN, IP Address, IP Range, or CIDR.
            start_time (datetime, optional): When the exclusion should start.
            end_time (datetime, optional): When the exclusion should end.
            description (str, optional):
                Some further detail about the exclusion.
            frequency (str, optional):
                The frequency of the rule. The string inputted will be upcased.
                Valid values are: *ONETIME, DAILY, WEEKLY, MONTHLY, YEARLY*.
            interval (int, optional): The interval of the rule.
            weekdays (list, optional):
                List of 2-character representations of the days of the week to
                repeat the frequency rule on.  Valid values are:
                *SU, MO, TU, WE, TH, FR, SA*
                Default values: ``['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']``
            day_of_month (int, optional):
                The day of the month to repeat a **MONTHLY** frequency rule on.
            enabled (bool, optional):
                enable/disable exclusion.
            network_id (uuid, optional):
                The ID of the network object associated with scanners
                where Tenable.io applies the exclusion.

        Returns:
            :obj:`dict`:
                Dictionary of the newly minted exclusion.

        Examples:
            Modifying the name of an exclusion:

            >>> exclusion = tio.v3.vm.exclusions.edit(1, name='New Name')
        '''

        # Lets start constructing the payload to be sent to the API...
        res_dict = self.details(exclusion_id=exclusion_id)

        if res_dict['schedule']['rrules'] is None:
            res_dict['schedule']['rrules'] = {}

        if enabled is None:
            enabled = res_dict['schedule']['enabled']

        payload: dict = {
            'name': name or res_dict['name'],
            'members': members or str(res_dict['members']).split(','),
            'description': description or res_dict['description'],
            'network_id': network_id or res_dict['network_id'],
            'schedule': {
                'enabled': enabled
            }
        }

        if payload['schedule']['enabled']:
            if isinstance(frequency, str):
                frequency = frequency.upper()

            # interval needs to be handled in schedule enabled excusion
            rrules = {
                'freq': frequency or res_dict['schedule']['rrules'].get(
                    'freq', ''
                ) or 'ONETIME',
                'interval': interval or res_dict['schedule']['rrules'].get(
                    'interval', ''
                ) or 1
            }

            if rrules['freq'] == 'WEEKLY':
                if weekdays is not None:
                    rrules['byweekday'] = weekdays
                else:
                    rrules['byweekday'] = res_dict['schedule']['rrules'].get(
                        'byweekday', 'SU,MO,TU,WE,TH,FR,SA'
                    ).split(',')

            if frequency == 'MONTHLY':
                if day_of_month is not None:
                    rrules['bymonthday'] = day_of_month
                else:
                    rrules['bymonthday'] = payload['schedule']['rrules'].get(
                        'bymonthday', datetime.today().day
                    )

            payload['schedule']['rrules'] = rrules

            payload['schedule']['starttime'] = \
                start_time or res_dict['schedule']['starttime']

            payload['schedule']['endtime'] = \
                end_time or res_dict['schedule']['endtime']

        # Let's validate the payload using marshmallow schema
        payload = self._schema.dump(self._schema.load(payload))

        return self._put(f'{exclusion_id}', json=payload)

    def exclusions_import(self, fobj: BinaryIO) -> None:
        '''
        Import exclusions into Tenable.io.

        :devportal:`exclusions: import <exclusions-import>`

        Args:
            fobj (FileObject):
                The file object of the exclusion(s) you wish to import.

        Returns:
            :obj:`None`:
                Returned if Tenable.io successfully imports the exclusion file.

        Examples:
            >>> with open('import_example.csv') as exclusion:
            ...     tio.v3.vm.exclusions.exclusions_import(exclusion)
        '''
        fid = self._api.v3.vm.files.upload(fobj)

        self._post('import', json={'file': fid})

    def search(self):
        raise NotImplementedError('This method will be implemented later.')
