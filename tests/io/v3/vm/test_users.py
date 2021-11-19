'''
Testing the Users endpoints
'''
import re
import responses


@responses.activate
def test_details(api):
    responses.add(responses.GET,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)'
                             ),
                  json={
                      "uuid": "60f73e4f-8983-41c2-a13c-39074cbb6229",
                      "id": 255,
                      "user_name": "user@example.com",
                      "username": "user@example.com",
                      "email": "user@example.com",
                      "name": "User One",
                      "type": "local",
                      "permissions": 64,
                      "roles": ["ADMIN"],
                      "last_login_attempt": 1569429971576,
                      "login_fail_count": 0,
                      "login_fail_total": 3,
                      "enabled": True,
                      "undeletable": False,
                      "two_factor": {
                          "sms_phone": "+15551236789",
                          "sms_enabled": 1,
                          "email_enabled": 0,
                      },
                      "group_uuids": [
                          "f3cd0bb2-cabb-4825-9d0c-49c77fe5fba7",
                          "00000000-0000-0000-0000-000000000000",
                          "2d5c70da-b177-43ed-8325-a25a846c8977",
                          "a507f383-3130-4c89-b202-b69ad9a75a84",
                          "afed07ce-8e51-4574-a420-90057fea6a7f",
                      ],
                      "lockout": 0,
                      "container_uuid": "270f77d7-3b5b-478c-ac06-be827c00753e",
                      "lastlogin": 1605630009020,
                      "uuid_id": "73cc516b-51d0-445a-8e0d-6f618455770e",
                  }
                  )
    details = api.v3.vm.users.details(255)
    assert isinstance(details, dict)
    assert details['uuid'] == "60f73e4f-8983-41c2-a13c-39074cbb6229"


@responses.activate
def test_delete(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)'
                             ),
                  json={}
                  )
    del_data = api.v3.vm.users.delete(255)
    assert isinstance(del_data, dict)


@responses.activate
def test_edit(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)'
                             ),
                  json={
                      "uuid": "1eddf745-7f6b-440a-90c6-df88efe2cf77",
                      "id": 4,
                      "user_name": "user3@example.com",
                      "username": "user3@example.com",
                      "email": "user3@example.com",
                      "name": "Test User",
                      "type": "local",
                      "container_uuid": "f8973c82-01a7-4aee-9754-4a61e3b3e70e",
                      "permissions": 32,
                      "login_fail_count": 0,
                      "login_fail_total": 0,
                      "enabled": False,
                      "lockout": 0,
                      "uuid_id": "1eddf745-7f6b-440a-90c6-df88efe2cf77"
                  }
                  )
    edit_data = api.v3.vm.users.edit(4, name='Test User')
    assert isinstance(edit_data, dict)
    assert edit_data['uuid'] == "1eddf745-7f6b-440a-90c6-df88efe2cf77"


@responses.activate
def test_enabled(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/enabled'
                             ),
                  json={
                      "object": "user"
                  }
                  )
    enabled_data = api.v3.vm.users.enabled(4, True)
    assert isinstance(enabled_data, dict)
    assert enabled_data['object'] == "user"


@responses.activate
def test_change_password(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/chpasswd'
                             ),
                  json={}
                  )
    change_pass_res = api.v3.vm.users.change_password(1, 'old_pass', 'new_pass')
    assert isinstance(change_pass_res, dict)


@responses.activate
def test_gen_api_keys(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/keys'
                             ),
                  json={
                      'accessKey': '2342sdfjsdfads86e1bc7a240ce398645cf2bb80bbbefc178f100d6f5ffc067d',
                      'secretKey': '876dfasdf6a87df6ad2910f1d54d23c14190a267285de4b05a481b1e6d3f0fd6'
                  }
                  )
    api_data = api.v3.vm.users.gen_api_keys(12345)
    assert isinstance(api_data, dict)
    assert api_data['access_key'] == '2342sdfjsdfads86e1bc7a240ce398645cf2bb80bbbefc178f100d6f5ffc067d'


@responses.activate
def test_create(api):
    responses.add(responses.POST,
                  re.compile(r'https://cloud.tenable.com/v3/users/'),
                  json={
                      "uuid": "d748ab37-f2cf-461c-8648-a8328c0f483e",
                      "id": 5,
                      "user_name": "user2@example.com",
                      "username": "user4@api.demo",
                      "email": "user2@example.com",
                      "name": "Test User",
                      "type": "local",
                      "aggregate": True,
                      "container_uuid": "f8973c82-01a7-4aee-9754-4a61e3b3e70e",
                      "permissions": 32,
                      "login_fail_count": 0,
                      "login_fail_total": 0,
                      "enabled": True,
                      "lockout": 0,
                      "uuid_id": "d748ab37-f2cf-461c-8648-a8328c0f483e"
                  }
                  )
    data = api.v3.vm.users.create('user4@api.demo', 'password', 32)
    assert isinstance(data, dict)
    assert data['username'] == 'user4@api.demo'


@responses.activate
def test_list_auths(api):
    responses.add(responses.GET,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/authorizations'
                             ),
                  json={
                      "account_uuid": "6c8ffd08-53dc-493e-9823-9f99d4adeab4",
                      "user_uuid": "4a5e55d6-fd20-465d-9a29-0f1f166d0f49",
                      "api_permitted": True,
                      "password_permitted": False,
                      "saml_permitted": True
                  }
                  )
    auths_data = api.v3.vm.users.list_auths('4a5e55d6-fd20-465d-9a29-0f1f166d0f49')
    assert isinstance(auths_data, dict)
    assert auths_data['account_uuid'] == '6c8ffd08-53dc-493e-9823-9f99d4adeab4'


@responses.activate
def test_edit_auths(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/authorizations'
                             ),
                  json={}
                  )
    data = api.v3.vm.users.edit_auths('4a5e55d6-fd20-465d-9a29-0f1f166d0f49')
    assert isinstance(data, dict)


@responses.activate
def test_enable_two_factor(api):
    responses.add(responses.POST,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/two-factor/send-verification'
                             ),
                  json={}
                  )
    data = api.v3.vm.users.enable_two_factor(12345, '9847484848', 'password')
    assert isinstance(data, dict)


@responses.activate
def test_verify_two_factor(api):
    responses.add(responses.POST,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/two-factor/verify-code'
                             ),
                  json={}
                  )
    data = api.v3.vm.users.verify_two_factor(12345, '9847484848')
    assert isinstance(data, dict)


@responses.activate
def test_two_factor(api):
    responses.add(responses.PUT,
                  re.compile(r'https://cloud.tenable.com/v3/users/'
                             r'([0-9a-fA-F\-]+)/two-factor'
                             ),
                  json={}
                  )
    data = api.v3.vm.users.two_factor(12345, True, True, '93949494959')
    assert isinstance(data, dict)
