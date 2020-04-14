import connexion
import six

from swagger_server.models.user_modi import UserModi  # noqa: E501
from swagger_server import util


def modify_user(UserName, body):  # noqa: E501
    """Modify user

    To modify a a username/Password  # noqa: E501

    :param UserName: Enter username 
    :type UserName: str
    :param body: Enter user name, password, option (1 for updating username, 2 for password), modification
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserModi.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
