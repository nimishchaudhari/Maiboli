import connexion
import six

from swagger_server.models.test_query import TestQuery  # noqa: E501
from swagger_server.models.user_query import UserQuery  # noqa: E501
from swagger_server import util
import enligne as el
import dix

def execute_query(body):  # noqa: E501
    """Queries for executing code

    This post type request should input the following in a json format query*  string lang*  string user_id*  string passwd*  string Query should not have double quotes in the code, since that&#x27;ll clash with the json double quotes lang codes:  mar - Marathi fr - French ur - Urdu gk - Greek  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserQuery.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def test_query(body):  # noqa: E501
    """Queries for executing code

    This post type request should input the following in a json format query*  string lang*  string user_id*  string passwd*  string Query should not have double quotes in the code, since that&#x27;ll clash with the json double quotes lang codes:  mar - Marathi fr - French ur - Urdu gk - Greek  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TestQuery.from_dict(connexion.request.get_json())  # noqa: E501
    eng = dix.en_final
    if(body.lang == "mar"):
        tgt = dix.mar_final
    return el.obj.execute(str(body.query),eng,tgt)
