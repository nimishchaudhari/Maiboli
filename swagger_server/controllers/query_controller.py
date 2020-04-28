import connexion
import six

from swagger_server.models.test_query import TestQuery  # noqa: E501
from swagger_server.models.user_query import UserQuery  # noqa: E501
from swagger_server import util
import enligne as el
import dix
import pyrebase
import swagger_server.controllers.user_controller as uc
import json
'''
Firebase essentials
'''

firebaseConfig = {
  "apiKey": "AIzaSyDNtFUjYR4pp09Vx526eDrcX4jjIvq-1XM",
  "authDomain": "maiboli-rest-api.firebaseapp.com",
  "databaseURL": "https://maiboli-rest-api.firebaseio.com",
  "projectId": "maiboli-rest-api",
  "storageBucket": "maiboli-rest-api.appspot.com",
  "messagingSenderId": "785641769787",
  "appId": "1:785641769787:web:1818d34874193d52ee051e",
  "measurementId": "G-WD78BEMMP3"
}
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("test@maiboli.fr", '123123')
db = firebase.database()
user = auth.refresh(user['refreshToken'])
token = user['idToken']


def execute_query(body):  # noqa: E501
    """Queries for executing code

    This post type request should input the following in a json format query*  string lang*  string user_id*  string passwd*  string Query should not have double quotes in the code, since that&#x27;ll clash with the json double quotes lang codes:  mar - Marathi fr - French ur - Urdu gk - Greek  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserQuery.from_dict(connexion.request.get_json())  # noqa: E501
    if (len(uc.login_mgmt.loggedin_user) == 1):
        #query = 'r"'+body.query+'"'
        op = el.obj.execute(body.query,dix.en,dix.select_dictionary(body.lang))      #Executing query

        data = {
            #str('"'+body.query+'"'):str('"'+op+'"')
            body.query : op
        }
        data = json.dumps(data)
        db.child("userlist").child(body.user_id).child("query").child(body.lang).push(data,token) #Updating query online with output
        return op


def test_query(body):  # noqa: E501
    """Queries for executing code

    This post type request should input the following in a json format query*  string lang*  string user_id*  string passwd*  string Query should not have double quotes in the code, since that&#x27;ll clash with the json double quotes lang codes:  mar - Marathi fr - French ur - Urdu gk - Greek  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TestQuery.from_dict(connexion.request.get_json())  # noqa: E501
    #eng = dix.en_final
    #if(body.lang == "mar"):
    #    tgt = dix.mar_final
    return 'not ok'#el.obj.execute(str(body.query),eng,tgt)

