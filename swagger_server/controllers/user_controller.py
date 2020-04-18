import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_modi import UserModi  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Creates a customer.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(id):  # noqa: E501
    """Delete user

    To delete a user entry # noqa: E501

    :param id: The username of the user that needs to be deleted
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_users():  # noqa: E501
    """Get Users

    Get all Users from the DB  # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def modify_user(body, id):  # noqa: E501
    """Modify user

    To modify a a username/Password  # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: The ID of the customer to delete.
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserModi.from_dict(connexion.request.get_json())  # noqa: E501

    return 'do some magic!'
