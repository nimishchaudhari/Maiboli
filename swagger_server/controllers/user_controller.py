import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_modi import UserModi  # noqa: E501
from swagger_server import util
import pyrebase


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


def create_user(body):  # noqa: E501
    """Creates a customer.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    #Trying with update(data)
    if(db.child("userlist").child(body.id).get().val()!= None):
        return str("Conflicts")
    else:
        db.child("userlist").child(body.id).child("id").set(str(body.id),token)
        db.child("userlist").child(body.id).child("pass").set(str(body.passwd),token)
    return str(body)


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
    users = db.child("userlist").get()
    print(users.val())
    return users.val()
    #return 'do some magic!'

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
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    if(db.child("userlist").child(id).get().val()!= None):
        #do stuff
        if(body.Option == 0):
            #Modify username
            db.child("userlist").child(body.id).update("{ 'id' : '"+body.Modification+"' }",token)
            db.child("userlist").update("{'userlist' : '"+body.Modification+"'}")
            #db.child("userlist").update("{'id':"+body.Modification+"}",token)
            return(db.child("userlist").child(body.Modification).get().val())
        elif(body.Option == 1):
            #Modify pass
            pass
        else:
            #Error
            pass
    else:
        return 404
    #return 'do some magic!'