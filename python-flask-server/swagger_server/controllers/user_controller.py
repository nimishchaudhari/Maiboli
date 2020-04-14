import connexion
import six
import pyrebase
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

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
db = firebase.database()
#users = db.child("user/test_user/").get()



def create_user(body):  # noqa: E501
    """Create User

     # noqa: E501

    :param body: To create a new user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    users = db.child("user").get()
    print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}
    #return users.val()
    return body
    #return 'do some magic!'


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
    users = db.child("user").get()
    print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}
    return users.val()
    #return 'do some magic!'

