from tenable.io.v3 import TenableIO
# from tenable.io import TenableIO


def tenable_connection():
    '''
    from tenable.io import TenableIO
    tio_t = TenableIO(
        "6625150eaec074271d23d3605cb838eaa8d9d40532e4a602271213389b2ea9af",
        "ca96ce21861d6839dc585692d22c2279a6ed7f12faefd40602f81df3aff73f0a",url ="https://qa-develop.cloud.aws.tenablesecurity.com")
    tio_t.filters.agents_filters()

    '''
    # access_key = '8ebe6067c6a4312cbaf849efffe3ed4829144f0d827bbd1038df11737e8cc631'
    # secret_key = 'cd7def442bc27f6f543be95cf49a6ecaebf849f00dfdbf87afbd5b19007b5016'
    access_key = "6625150eaec074271d23d3605cb838eaa8d9d40532e4a602271213389b2ea9af"
    secret_key = "ca96ce21861d6839dc585692d22c2279a6ed7f12faefd40602f81df3aff73f0a"
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
    users = tio.users.details(2236708)
    # users = tio.v3.users.list()
    for user in users:
        print(user)

get_users_v3()