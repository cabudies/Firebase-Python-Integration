# Read Data from Firebase to Python

# importing pyrebase library into python
import pyrebase

# configuring your firebase database
config = {

  #credentials taken from firebase 'Web Setup'

  "apiKey": "************************c", 
  "authDomain": "************************.firebaseapp.com",
  "databaseURL": "************************.firebaseio.com",
  "storageBucket": "************************.appspot.com"
}

firebase = pyrebase.initialize_app(config)

################## simple way to fetch data
fb = firebase.database()

result = fb.child("/python").get()
print("Firebase Data = %s" % result.val())
