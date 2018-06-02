# Read Data from Firebase to Python

# importing pyrebase library into python
import pyrebase

# configuring your firebase database
config = {

  #credentials taken from firebase 'Web Setup'

  "apiKey": "AIzaSyD2UCfuM-iFiMBKBT9uHfeSuNct5b-a4Wc", 
  "authDomain": "city-tour-guide-5f8f0.firebaseapp.com",
  "databaseURL": "https://city-tour-guide-5f8f0.firebaseio.com",
  "storageBucket": "city-tour-guide-5f8f0.appspot.com"
}

firebase = pyrebase.initialize_app(config)

################## simple way to fetch data
fb = firebase.database()

result = fb.child("/python").get()
print("Firebase Data = %s" % result.val())
