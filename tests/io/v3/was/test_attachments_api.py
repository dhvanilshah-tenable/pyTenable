'''
Testing the Attachments endpoints
'''
import os
import re

import responses

ATTACHMENTS_BASE_URL = r'https://cloud.tenable.com/api/v3/was/attachments'
USERS_API_ID = r'([0-9a-fA-F\-]+)'

dir_name = os.path.dirname(os.path.abspath(__file__))

IMG_ATTACHMENT_FILE = 'img_attachment_file.png'
TXT_ATTACHMENT_FILE = 'text_attachment_file.txt'

IMG_ATTACHMENT_FILE_PATH = os.path.join(dir_name, IMG_ATTACHMENT_FILE)
TXT_ATTACHMENT_FILE_PATH = os.path.join(dir_name, TXT_ATTACHMENT_FILE)

IMG_ATTACHMENT_ID = 'b1b335cf-938f-462a-b83d-088b72428a2a'
TXT_ATTACHMENT_ID = '49484c93-baa5-4952-8043-9afad238cb7b'

IMG_CONTENTS = None
TXT_CONTENTS = None


@responses.activate
def test_download_img_attachment(api):

    global IMG_CONTENTS

    if IMG_CONTENTS is None:
        with open(IMG_ATTACHMENT_FILE_PATH, 'rb') as img_file:
            IMG_CONTENTS = img_file.read()

    responses.add(
        responses.GET,
        re.compile(f'{ATTACHMENTS_BASE_URL}/{IMG_ATTACHMENT_FILE}'),
        body=IMG_CONTENTS
    )

    resp = api.v3.was.attachments.download_attachment(IMG_ATTACHMENT_FILE)
    assert resp.read() == IMG_CONTENTS


@responses.activate
def test_download_img_file_attachment(api):

    global IMG_CONTENTS

    if IMG_CONTENTS is None:
        with open(IMG_ATTACHMENT_FILE_PATH, 'rb') as img_file:
            IMG_CONTENTS = img_file.read()

    responses.add(
        responses.GET,
        re.compile(f'{ATTACHMENTS_BASE_URL}/{IMG_ATTACHMENT_FILE}'),
        body=IMG_CONTENTS
    )

    output_img_file_name = 'img_output_file.png'
    with open(output_img_file_name, 'wb') as img_file:
        api.v3.was.attachments.download_attachment(
            IMG_ATTACHMENT_FILE,
            img_file
        )

    with open(output_img_file_name, 'rb') as img_output:
        assert img_output.read() == IMG_CONTENTS

    os.remove(output_img_file_name)


@responses.activate
def test_download_txt_attachment(api):

    global TXT_CONTENTS

    if TXT_CONTENTS is None:
        with open(TXT_ATTACHMENT_FILE_PATH, 'rb') as txt_file:
            TXT_CONTENTS = txt_file.read()

    responses.add(
        responses.GET,
        re.compile(f'{ATTACHMENTS_BASE_URL}/{TXT_ATTACHMENT_FILE}'),
        body=TXT_CONTENTS
    )

    resp = api.v3.was.attachments.download_attachment(TXT_ATTACHMENT_FILE)
    assert resp.read() == TXT_CONTENTS


@responses.activate
def test_download_txt_file_attachment(api):

    global TXT_CONTENTS

    if TXT_CONTENTS is None:
        with open(TXT_ATTACHMENT_FILE_PATH, 'rb') as txt_file:
            TXT_CONTENTS = txt_file.read()

    responses.add(
        responses.GET,
        re.compile(f'{ATTACHMENTS_BASE_URL}/{TXT_ATTACHMENT_FILE}'),
        body=TXT_CONTENTS
    )

    output_txt_file_name = 'txt_output_file.txt'
    with open(output_txt_file_name, 'wb') as txt_file:
        api.v3.was.attachments.download_attachment(
            TXT_ATTACHMENT_FILE,
            txt_file
        )

    with open(output_txt_file_name, 'rb') as txt_output:
        assert txt_output.read() == TXT_CONTENTS

    os.remove(output_txt_file_name)
