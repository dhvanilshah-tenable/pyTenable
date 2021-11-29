'''
Testing the users schemas
'''
import pytest
from marshmallow.exceptions import ValidationError
from tenable.io.v3.schema import (
    UserEditSchema,
    UsersCreateSchema,
)
from tenable.io.v3.vm.schema import TargetGroupsSchema
from .test_target_groups import TARGET_GROUP


@pytest.fixture
def users_create():
    '''
    Example users create request
    '''
    return {
        'username': 'test_username',
        'password': 'password',
        'permissions': 32,
        'name': 'test',
        'email': 'test@tenable.com',
        'type': 'local'
    }


@pytest.fixture
def target_group():
    '''
    Example target group
    '''
    return {
        'name': TARGET_GROUP['name'],
        'members': TARGET_GROUP['members'],
        'acls': TARGET_GROUP['acls']
    }


@pytest.fixture
def users_edit():
    '''
    Example users edit request
    '''
    return {
        'permissions': 32,
        'name': 'test',
        'email': 'test@tenable.com',
        'enabled': True
    }


def test_users_create_schema(users_create):
    '''
    Test the users create schema
    '''
    test_resp = {
        'username': 'test_username',
        'password': 'password',
        'permissions': 32,
        'name': 'test',
        'email': 'test@tenable.com',
        'type': 'local'
    }

    schema = UsersCreateSchema()
    assert test_resp == schema.dump(schema.load(users_create))

    with pytest.raises(ValidationError):
        users_create['new_val'] = 'something'
        schema.load(users_create)


def test_users_edit_schema(users_edit):
    '''
    Test the users create schema
    '''
    test_resp = {
        'permissions': 32,
        'name': 'test',
        'email': 'test@tenable.com',
        'enabled': True
    }

    schema = UserEditSchema()
    assert test_resp == schema.dump(schema.load(users_edit))

    with pytest.raises(ValidationError):
        users_edit['new_val'] = 'something'
        schema.load(users_edit)


def test_target_groups_schema(target_group):
    '''
    Test the target groups create schema
    '''
    schema = TargetGroupsSchema()
    assert target_group == schema.dump(schema.load(target_group))

    with pytest.raises(ValidationError):
        target_group['new_val'] = 'something'
        schema.load(target_group)
