import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Create User

     # noqa: E501

    :param body: To create a new user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(UserName, body):  # noqa: E501
    """Delete user

    To delete a user entry # noqa: E501

    :param UserName: The username of the user that needs to be deleted
    :type UserName: str
    :param body: Password needed to delete a user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_users(body):  # noqa: E501
    """Get Users

    Get all Users from the DB  # noqa: E501

    :param body: To create a new user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
