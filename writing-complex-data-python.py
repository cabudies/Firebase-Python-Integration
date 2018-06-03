import pyrebase

# configuring your firebase database
config = {
  
  # credentials taken from Firebase 'Web-Setup'
  
  "apiKey": "************************c",
  "authDomain": "************************.firebaseapp.com",
  "databaseURL": "************************.firebaseio.com",
  "storageBucket": "************************.appspot.com"
}

# initializing the firebase object
firebase = pyrebase.initialize_app(config)

# providing the login details for the Authentication
# we need to provide login details because as per the rules of firebase, we cannot write anything until
# unless the user is not authorized user.

email = 'brillicaservice@gmail.com'
password = "Brillica@92G!"

# initializing an auth variable that will authorize the app
auth = firebase.auth()

# try catch functionality in case the login details are incorrect.
try:

    # use this function to sign in with email and password
    user = auth.sign_in_with_email_and_password(email, password)
    
    # after authorization, initializing the firebase databse.
    fb = firebase.database()
    
    # writing the data into a JSON structure i.e. key-value pair
    data = {
        "name": "Rohit",
        "course": "Python",
        "fees-paid": "True"
    }

    # telling firebase where to put this data
    # as of now, we are inserting this data into 'Students-List' node and 
    # sending the authenticated user token as well while pushing the new data
    fb.child("students-list").push(data, user['idToken'])
    
    # print succcess message once the data has been pushed successfully
    print('New value inserted successfully')
    
# incase there is any exception that has raised    
except Exception:
    print('Sorry some error occurred. Please try again later.')
