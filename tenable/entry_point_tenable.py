# from tenable.io.v3 import TenableIO
from tenable.io import TenableIO
'''
This is a test file for development purpose only
'''

def tenable_connection():
    '''
    from tenable.io import TenableIO
    tio_t = TenableIO(
        "6625150eaec074271d23d3605cb838eaa8d9d40532e4a602271213389b2ea9af",
        "ca96ce21861d6839dc585692d22c2279a6ed7f12faefd40602f81df3aff73f0a",url ="https://qa-develop.cloud.aws.tenablesecurity.com")
    tio_t.filters.agents_filters()

    '''

    access_key = "0fb9443503651ebd8050a87a5a133ba4665002e703caabde280a887ea0116b20"
    secret_key = "5f7b11c7411591b569d08201a18795492e4d93d4d64512657925a95e0643616f"
    url = "https://qa-develop.cloud.aws.tenablesecurity.com"
    container_uuid = 'cfdabb09-6aef-481d-b28f-aecb1c38f297'
    tio = TenableIO(access_key=access_key, secret_key=secret_key, url=url)
    return tio


def get_users():
    tio = tenable_connection()
    # users = tio.users.list()
    users = tio.filters.agents_filters()
    for user in users:
        print(user)

def get_users_v3():
    tio = tenable_connection()
    # users = tio.v3.vm.users.details(user_id="2236708tes")
    users = tio.v3.vm.users.edit(user_id=2236708, permissions=12)
    # users = tio.v3.users.list()
    for user in users:
        print(user)

def create_users_v3():
    tio = tenable_connection()
    # users = tio.v3.vm.users.details("2236708tes")
    # users = tio.v3.users.list()
    user = tio.v3.vm.users.create(username="sahil", password="test", permissions=12)
    print(user)

def get_networks_v3():
    tio = tenable_connection()
    # neto = tio.networks.list(("name", "eq", "Default"))
    # print(neto)
    neto = tio.v3.vm.users.search_users(("name", "eq", "sahilsingh"), fields=["name", "uuid", "last_login"],
                                        limit=10)
    print(neto)

def export_vulns():
    tio = tenable_connection()
    vulns = tio.exports.vulns()
    for vu in vulns:
        print(vu)
    print(vulns)

get_users_v3()